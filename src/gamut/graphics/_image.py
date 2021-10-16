
__all__ = ['Image']

# gamut
from ._texture2d import Texture2d, TextureComponents, TextureDataType
# python
from pathlib import Path
from typing import BinaryIO, Final, Union
from PIL import Image as PilImage
from PIL import ImageMath as PilImageMath

PIL_MODE_TO_TEXTURE_COMPONENTS: Final = {
    'L': TextureComponents.R,
    'RGB': TextureComponents.RGB,
    'RGBA': TextureComponents.RGBA,
}


PIL_MODE_TO_COMPONENTS: Final = {
    'L': 1,
    'RGB': 3,
    'RGBA': 4,
}


PIL_CONVERT: Final = {
    '1': 'L',
    'LA': 'RGBA',
    'CMYK': 'RGBA',
    'YCbCr': 'RGB',
    'LAB': 'RGB',
    'HSV': 'RGB',
}


class Image:

    def __init__(self, file: Union[str, Path, BinaryIO]):
        self._pil = PilImage.open(file)

        # we "normalize" the image to an R, RGB, or RGBA mode so that the
        # bytes representation is predictable
        convert_mode = self._pil.mode
        if convert_mode in ['I', 'F']:
            # I and F should convert to L, but pillow has some isues with this,
            # so we must to it manually
            # https://github.com/python-pillow/Pillow/issues/3011
            self._pil = PilImageMath.eval(
                'image >> 8',
                image=self._pil.convert('I')
            ).convert('L')
            convert_mode = 'L'
        # P/PA are palette modes, so use whatever the mode is of the palette
        if convert_mode in ['P', 'PA']:
            convert_mode = self._pil.palette.mode
        if convert_mode not in PIL_MODE_TO_TEXTURE_COMPONENTS:
            try:
                convert_mode = PIL_CONVERT[convert_mode]
            except KeyError:
                raise RuntimeError('invalid image')
        if convert_mode != self._pil.mode:
            self._pil = self._pil.convert(mode=convert_mode)

        self._components = PIL_MODE_TO_COMPONENTS[self._pil.mode]

    def _ensure_open(self) -> None:
        if self._pil is None:
            raise RuntimeError('image is closed')

    def to_bytes(self) -> bytes:
        self._ensure_open()
        result: bytes = self._pil.tobytes()
        assert isinstance(result, bytes)
        return result

    def to_texture(self) -> Texture2d:
        self._ensure_open()
        return Texture2d(
            *self.size,
            PIL_MODE_TO_TEXTURE_COMPONENTS[self._pil.mode],
            TextureDataType.UNSIGNED_BYTE,
            self.to_bytes()
        )

    def close(self) -> None:
        if self._pil is not None:
            self._pil.close()
            self._pil = None

    @property
    def components(self) -> int:
        return self._components

    @property
    def is_open(self) -> bool:
        return self._pil is not None

    @property
    def size(self) -> tuple[int, int]:
        self._ensure_open()
        size: tuple[int, int] = self._pil.size
        assert isinstance(size, tuple)
        assert len(size) == 2
        return size
