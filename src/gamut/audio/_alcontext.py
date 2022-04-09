
from __future__ import annotations

__all__ = [
    'AlContext',
    'LOOP_BACK_AVAILABLE',
    'LOOP_BACK_FREQUENCY',
    'get_al_context',
    'require_al_context',
    'release_al_context',
]

# python
# DVector4
from ctypes import c_char, c_char_p, c_int, c_ubyte, c_void_p
from threading import Lock
import time
from typing import Any, Final, Optional
# pyopenal
from openal.al_lib import lib as al_lib
from openal.alc import (alc_check_error, ALC_FREQUENCY, alcCloseDevice,
                        alcCreateContext, alcDestroyContext,
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
    ALC_STEREO_SOFT = 0x1501
    ALC_UNSIGNED_BYTE_SOFT = 0x1401

    _loop_back_available = True
except AttributeError:
    _loop_back_available = False


LOOP_BACK_AVAILABLE: Final = _loop_back_available
LOOP_BACK_FREQUENCY: Final = 44100


class AlContext:

    def __init__(self, loopback: bool) -> None:
        self._loopback = loopback
        if loopback:
            assert LOOP_BACK_AVAILABLE
            self._al_device = alcLoopbackOpenDeviceSOFT(None)
            alcIsRenderFormatSupportedSOFT(
                self._al_device,
                LOOP_BACK_FREQUENCY,
                ALC_STEREO_SOFT,
                0x1401,
            )
            context_attributes = [
                ALC_FORMAT_CHANNELS_SOFT, ALC_STEREO_SOFT,
                ALC_FORMAT_TYPE_SOFT, ALC_UNSIGNED_BYTE_SOFT,
                ALC_FREQUENCY, LOOP_BACK_FREQUENCY,
            ]
        else:
            self._al_device = alcOpenDevice(None)
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
        alcMakeContextCurrent(self._al_context)

    def render(
        self,
        samples: int,
        *,
        real_time: bool = False
    ) -> tuple[bytes, bytes]:
        assert self._loopback
        if not real_time:
            buffer = (c_ubyte * samples * 2)()
            alcRenderSamplesSOFT(self._al_device, buffer, samples)
            stereo = bytes(buffer)
            return (stereo[::2], stereo[1::2])
        else:
            step_frames = LOOP_BACK_FREQUENCY // 50
            left = bytearray()
            right = bytearray()
            for i in range(samples // step_frames):
                t_left, t_right = self.render(step_frames)
                left += t_left
                right += t_right
                time.sleep(1 / 50.0)
            leftover_frames = samples % step_frames
            if leftover_frames:
                t_left, t_right = self.render(leftover_frames)
                left += t_left
                right += t_right
                time.sleep(1 / 50.0)
            return (bytes(left), bytes(right))


    def close(self) -> None:
        if hasattr(self, "_al_context") and self._al_context:
            alcDestroyContext(self._al_context)
            self._al_context = None
        if hasattr(self, "_al_device") and self._al_device:
            alcCloseDevice(self._al_device)


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
