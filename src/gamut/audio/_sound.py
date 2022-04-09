
__all__ = ['Sound']


# gamut
from ._source import Sample, Stream
# python
# DVector4
from abc import ABC, abstractmethod
from pathlib import Path
from typing import BinaryIO, Optional, Union
import wave


class Sound:

    def __init__(self, file: Union[str, Path, BinaryIO]):
        self._owns_file = False
        self._file: Optional[BinaryIO] = None
        self._impl: Optional[SoundImplementation] = None

        if isinstance(file, (str, Path)):
            self._file = open(file, 'rb')
            self._owns_file = True
        else:
            self._file = file

        start = self._file.tell()
        header = self._file.read(4)
        self._file.seek(start)
        if header == b'RIFF':
            self._impl = WaveImplementation(self._file)
        else:
            raise ValueError('unable to determine sound format')

    def __len__(self) -> int:
        self._ensure_open()
        assert self._impl is not None
        return len(self._impl)

    def __del__(self) -> None:
        self.close()

    def _ensure_open(self) -> None:
        if self._file is None or self._impl is None:
            raise RuntimeError('sound is closed')

    def close(self) -> None:
        if hasattr(self, "_impl") and self._impl is not None:
            self._impl.close()
            self._impl = None
        if self._owns_file and self._file is not None:
            self._file.close()
        self._file = None

    @property
    def channels(self) -> int:
        self._ensure_open()
        assert self._impl is not None
        return self._impl.get_channels()

    @property
    def sample_width(self) -> int:
        self._ensure_open()
        assert self._impl is not None
        return self._impl.get_sample_width()

    @property
    def sample_rate(self) -> int:
        self._ensure_open()
        assert self._impl is not None
        return self._impl.get_sample_rate()

    @property
    def is_open(self) -> bool:
        return self._file is not None

    def read(self, frames: int = 0) -> bytes:
        self._ensure_open()
        assert self._impl is not None
        if frames == 0:
            result = bytearray()
            while True:
                chunk = self._impl.read(1024)
                if not chunk:
                    break
                result += chunk
            return bytes(result)
        else:
            return self._impl.read(frames)

    def seek(self, frame: int) -> None:
        self._ensure_open()
        assert self._impl is not None
        return self._impl.seek(frame)

    def tell(self) -> int:
        self._ensure_open()
        assert self._impl is not None
        return self._impl.tell()

    def to_sample(self) -> Sample:
        start = self.tell()
        self.seek(0)
        sample = Sample(
            self.channels,
            self.sample_width,
            self.sample_rate,
            self.read(),
        )
        self.seek(start)
        return sample

    def to_stream(self) -> Stream:
        return Stream(
            self.channels,
            self.sample_width,
            self.sample_rate,
            self,
        )


class SoundImplementation(ABC):

    def __del__(self) -> None:
        self.close()

    @abstractmethod
    def __len__(self) -> int:
        ...

    def close(self) -> None:
        pass

    @abstractmethod
    def get_channels(self) -> int:
        ...

    @abstractmethod
    def get_sample_width(self) -> int:
        ...

    @abstractmethod
    def get_sample_rate(self) -> int:
        ...

    @abstractmethod
    def read(self, frames: int) -> bytes:
        ...

    @abstractmethod
    def seek(self, frame: int) -> None:
        ...

    @abstractmethod
    def tell(self) -> int:
        ...


class WaveImplementation(SoundImplementation):

    def __init__(self, file: BinaryIO):
        super().__init__()
        self._wave = wave.open(file)

    def __len__(self) -> int:
        length = self._wave.getnframes()
        assert isinstance(length, int)
        return length

    def close(self) -> None:
        self._wave.close()
        super().close()

    def get_channels(self) -> int:
        channels = self._wave.getnchannels()
        assert isinstance(channels, int)
        return channels

    def get_sample_width(self) -> int:
        sample_width = self._wave.getsampwidth()
        assert isinstance(sample_width, int)
        return sample_width * 8

    def get_sample_rate(self) -> int:
        sample_rate = self._wave.getframerate()
        assert isinstance(sample_rate, int)
        return sample_rate

    def read(self, frames: int) -> bytes:
        data = self._wave.readframes(frames)
        assert isinstance(data, bytes)
        return data

    def seek(self, frame: int) -> None:
        self._wave.setpos(frame)

    def tell(self) -> int:
        where = self._wave.tell()
        assert isinstance(where, int)
        return where
