
# gamut
from gamut.audio import Sample, Sound, Stream
from gamut.audio._alcontext import AlContext
# python
from io import BytesIO
import os
from pathlib import Path
from typing import Any, BinaryIO, Final, Union
# pytest
import pytest

DIR: Final = Path(__file__).parent


class SoundTest:

    def __init_subclass__(
        cls,
        *,
        file_path: str,
        channels: int,
        sample_width: int,
        sample_rate: int,
        length: int,
    ) -> None:
        with open(file_path, 'rb') as f:
            file_bytes = f.read()
        def generate_files() -> list[Any]:
            return [
                pytest.param(str(file_path), id='str'),
                pytest.param(Path(file_path), id='Path'),
                pytest.param(BytesIO(file_bytes), id='BytesIO'),
            ]

        @pytest.mark.parametrize("file", generate_files())
        def test_initialize(
            self: SoundTest,
            file: Union[str, Path, BinaryIO]
        ) -> None:
            sound = Sound(file)
            assert len(sound) == length
            assert sound.channels == channels
            assert sound.sample_width == sample_width
            assert sound.sample_rate == sample_rate
            assert sound.tell() == 0
            assert sound.is_open
        cls.test_initialize = test_initialize # type: ignore

        @pytest.mark.parametrize("file", generate_files())
        def test_read_seek_tell(
            self: SoundTest,
            file: Union[str, Path, BinaryIO]
        ) -> None:
            sound = Sound(file)
            assert sound.tell() == 0

            data = sound.read()
            assert len(data) == length * channels * (sample_width // 8)
            assert sound.tell() == len(sound)

            sound.seek(0)
            assert sound.tell() == 0
            assert sound.read(0) == data

            assert sound.read() == b''

            seek_data_index = 10 * channels * (sample_width // 8)
            read_data_index = seek_data_index * 2
            sound.seek(10)
            assert sound.read(10) == data[seek_data_index:read_data_index]
        cls.test_read_seek_tell = test_read_seek_tell # type: ignore

        @pytest.mark.parametrize("file", generate_files())
        def test_to_sample(
            self: SoundTest,
            loopback_al_context: AlContext,
            file: Union[str, Path, BinaryIO]
        ) -> None:
            sound = Sound(file)
            if sound.sample_width not in [8, 16]:
                pytest.xfail('only 8 and 16 bit samples supported')
            sample = sound.to_sample()
            assert isinstance(sample, Sample)
            assert sample.channels == sound.channels
            assert sample.sample_width == sound.sample_width
            assert sample.sample_rate == sound.sample_rate
        cls.test_to_sample = test_to_sample # type: ignore

        @pytest.mark.parametrize("file", generate_files())
        def test_to_stream(
            self: SoundTest,
            loopback_al_context: AlContext,
            file: Union[str, Path, BinaryIO]
        ) -> None:
            sound = Sound(file)
            if sound.sample_width not in [8, 16]:
                pytest.xfail('only 8 and 16 bit samples supported')
            stream = sound.to_stream()
            assert isinstance(stream, Stream)
            assert stream.channels == sound.channels
            assert stream.sample_width == sound.sample_width
            assert stream.sample_rate == sound.sample_rate
        cls.test_to_stream = test_to_stream # type: ignore

        @pytest.mark.parametrize("file", generate_files())
        def test_close(
            self: SoundTest,
            file: Union[str, Path, BinaryIO]
        ) -> None:
            sound = Sound(file)
            assert sound.is_open

            sound.close()
            assert not sound.is_open

            sound.close()
            assert not sound.is_open

            with pytest.raises(RuntimeError) as excinfo:
                len(sound)
            assert str(excinfo.value) == 'sound is closed'

            with pytest.raises(RuntimeError) as excinfo:
                sound.channels
            assert str(excinfo.value) == 'sound is closed'

            with pytest.raises(RuntimeError) as excinfo:
                sound.sample_width
            assert str(excinfo.value) == 'sound is closed'

            with pytest.raises(RuntimeError) as excinfo:
                sound.sample_rate
            assert str(excinfo.value) == 'sound is closed'

            with pytest.raises(RuntimeError) as excinfo:
                sound.read()
            assert str(excinfo.value) == 'sound is closed'

            with pytest.raises(RuntimeError) as excinfo:
                sound.seek(10)
            assert str(excinfo.value) == 'sound is closed'

            with pytest.raises(RuntimeError) as excinfo:
                sound.tell()
            assert str(excinfo.value) == 'sound is closed'

            with pytest.raises(RuntimeError) as excinfo:
                sound.to_sample()
            assert str(excinfo.value) == 'sound is closed'

            with pytest.raises(RuntimeError) as excinfo:
                sound.to_stream()
            assert str(excinfo.value) == 'sound is closed'
        cls.test_close = test_close # type: ignore


def test_unable_to_load() -> None:
    with pytest.raises(ValueError) as excinfo:
        Sound(BytesIO(b''))
    assert str(excinfo.value) == 'unable to determine sound format'


for file_name in os.listdir(DIR / 'sounds'):
    name, extension = file_name.split('.')
    channels, sample_width, sample_rate, length = [
        int(p) for p in name.split('-')
    ]
    class _SoundTest(
        SoundTest,
        file_path=str(DIR / 'sounds' / file_name),
        channels=channels,
        sample_width=sample_width,
        sample_rate=sample_rate,
        length=length,
    ):
        pass
    globals()[
        f'Test{channels}Channel{sample_width}SampleWidth{sample_rate}'
        f'SampleRate{length}Length{extension.capitalize()}'
    ] = _SoundTest
