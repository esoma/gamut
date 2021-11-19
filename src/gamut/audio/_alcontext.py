
from __future__ import annotations

__all__ = [
    'AlContext',
    'LOOP_BACK_AVAILABLE',
    'get_al_context',
    'require_al_context',
    'release_al_context',
]

# python
from ctypes import c_char, c_char_p, c_int, c_ubyte, c_void_p
from threading import Lock
from typing import Any, Final, Optional
# pyopenal
from openal.al_lib import lib as al_lib
from openal.alc import (alc_check_error, ALC_FALSE, ALC_FREQUENCY,
                        alcCloseDevice, alcCreateContext, alcDestroyContext,
                        alcMakeContextCurrent, alcOpenDevice)

singleton: Optional[AlContext] = None
refs_lock = Lock()
refs: int = 0


# ALC_SOFT_loopback
try:
    alcLoopbackOpenDeviceSOFT = al_lib.alcLoopbackOpenDeviceSOFT
    alcLoopbackOpenDeviceSOFT.argtypes = [c_char_p]
    alcLoopbackOpenDeviceSOFT.restype = c_void_p
    alcLoopbackOpenDeviceSOFT.errcheck = alc_check_error

    alcIsRenderFormatSupportedSOFT = al_lib.alcIsRenderFormatSupportedSOFT
    alcIsRenderFormatSupportedSOFT.argtypes = [c_void_p, c_int, c_int, c_int]
    alcIsRenderFormatSupportedSOFT.restype = c_char
    alcIsRenderFormatSupportedSOFT.errcheck = alc_check_error

    alcRenderSamplesSOFT = al_lib.alcRenderSamplesSOFT
    alcRenderSamplesSOFT.argtypes = [c_void_p, c_void_p, c_int]
    alcRenderSamplesSOFT.restype = None
    alcIsRenderFormatSupportedSOFT.errcheck = alc_check_error

    ALC_FORMAT_CHANNELS_SOFT = 0x1990
    ALC_FORMAT_TYPE_SOFT = 0x1991

    ALC_MONO_SOFT = 0x1500
    ALC_UNSIGNED_BYTE_SOFT = 0x1401

    _loop_back_available = True
except AttributeError:
    _loop_back_available = False


LOOP_BACK_AVAILABLE: Final = _loop_back_available


class AlContext:

    def __init__(self, loopback: bool) -> None:
        self._loopback = loopback
        if loopback:
            assert LOOP_BACK_AVAILABLE
            self._al_device = alcLoopbackOpenDeviceSOFT(None)
            if not self._al_device:
                raise RuntimeError('unable to open audio device')
            if alcIsRenderFormatSupportedSOFT(
                self._al_device,
                22050,
                ALC_MONO_SOFT,
                0x1401,
            ) == ALC_FALSE:
                raise RuntimeError('loopback device format not available')
            context_attributes = [
                ALC_FORMAT_CHANNELS_SOFT, ALC_MONO_SOFT,
                ALC_FORMAT_TYPE_SOFT, ALC_UNSIGNED_BYTE_SOFT,
                ALC_FREQUENCY, 22050,
            ]
        else:
            self._al_device = alcOpenDevice(None)
            if not self._al_device:
                raise RuntimeError('unable to open audio device')
            context_attributes = []


        if not context_attributes:
            c_context_attributes = None
        else:
            c_context_attributes = (c_int * (len(context_attributes) + 1))(
                *context_attributes,
                0
            )
        self._al_context = alcCreateContext(
            self._al_device,
            c_context_attributes
        )
        if not self._al_context:
            raise RuntimeError('unable to create OpenAL context')
        if not alcMakeContextCurrent(self._al_context):
            raise RuntimeError('unable to make OpenAL context current')

    def render(self, samples: int) -> bytes:
        assert self._loopback
        buffer = (c_ubyte * samples)()
        alcRenderSamplesSOFT(self._al_device, buffer, samples)
        return bytes(buffer)

    def close(self) -> None:
        if hasattr(self, "_al_context") and self._al_context:
            alcDestroyContext(self._al_context)
            self._al_context = None
        if hasattr(self, "_al_device") and self._al_device:
            if alcCloseDevice(self._al_device) == ALC_FALSE:
                raise RuntimeError('unable to cleanup OpenAL device')


def release_al_context(al_context_marker: Any) -> Any:
    global singleton
    global refs
    if al_context_marker != 1:
        return False
    with refs_lock:
        assert singleton is not None
        assert refs > 0
        refs -= 1
        if refs == 0:
            singleton.close()
            assert refs == 0
            singleton = None
    return False


def require_al_context(*, loopback: bool = False) -> Any:
    global refs
    global singleton
    with refs_lock:
        if singleton is None:
            assert refs == 0
            singleton = AlContext(loopback)
        else:
            assert not loopback
        refs += 1
    return True


def get_al_context() -> AlContext:
    with refs_lock:
        if singleton is None:
            raise RuntimeError('no al context')
        return singleton
