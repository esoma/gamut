
from __future__ import annotations

__all__ = [
    'Keyboard',
    'KeyboardKey',
    'KeyboardKeyEvent',
    'KeyboardKeyPressed',
    'KeyboardKeyReleased',
    'KeyboardConnected',
    'KeyboardDisconnected',
    'KeyboardEvent',
    'KeyboardLostFocus',
    'KeyboardFocused',
    'PressableKeyboardKey',
]

# gamut
from ._peripheral import (Peripheral, PeripheralConnected,
                          PeripheralDisconnected, PeripheralEvent)
# gamut
from gamut._sdl import sdl_event_callback_map, sdl_window_event_callback_map
from gamut._window import get_window_from_sdl_id, Window
# python
import platform
from typing import Any, ClassVar, Final, Optional, TYPE_CHECKING
from weakref import ref
# pysdl2
import sdl2
from sdl2 import (SDL_KEYDOWN, SDL_KEYUP, SDL_SCANCODE_UNKNOWN,
                  SDL_WINDOWEVENT_FOCUS_GAINED, SDL_WINDOWEVENT_FOCUS_LOST)

if TYPE_CHECKING:
    # gamut
    from ._controller import Controller
    from ._mouse import Mouse


sdl_scancode_to_gamut_key_name: Final = {
    # number
    sdl2.SDL_SCANCODE_0: 'zero',
    sdl2.SDL_SCANCODE_1: 'one',
    sdl2.SDL_SCANCODE_2: 'two',
    sdl2.SDL_SCANCODE_3: 'three',
    sdl2.SDL_SCANCODE_4: 'four',
    sdl2.SDL_SCANCODE_5: 'five',
    sdl2.SDL_SCANCODE_6: 'six',
    sdl2.SDL_SCANCODE_7: 'seven',
    sdl2.SDL_SCANCODE_8: 'eight',
    sdl2.SDL_SCANCODE_9: 'nine',
    # function
    sdl2.SDL_SCANCODE_F1: 'f1',
    sdl2.SDL_SCANCODE_F2: 'f2',
    sdl2.SDL_SCANCODE_F3: 'f3',
    sdl2.SDL_SCANCODE_F4: 'f4',
    sdl2.SDL_SCANCODE_F5: 'f5',
    sdl2.SDL_SCANCODE_F6: 'f6',
    sdl2.SDL_SCANCODE_F7: 'f7',
    sdl2.SDL_SCANCODE_F8: 'f8',
    sdl2.SDL_SCANCODE_F9: 'f9',
    sdl2.SDL_SCANCODE_F10: 'f10',
    sdl2.SDL_SCANCODE_F11: 'f11',
    sdl2.SDL_SCANCODE_F12: 'f12',
    sdl2.SDL_SCANCODE_F13: 'f13',
    sdl2.SDL_SCANCODE_F14: 'f14',
    sdl2.SDL_SCANCODE_F15: 'f15',
    sdl2.SDL_SCANCODE_F16: 'f16',
    sdl2.SDL_SCANCODE_F17: 'f17',
    sdl2.SDL_SCANCODE_F18: 'f18',
    sdl2.SDL_SCANCODE_F19: 'f19',
    sdl2.SDL_SCANCODE_F20: 'f20',
    sdl2.SDL_SCANCODE_F21: 'f21',
    sdl2.SDL_SCANCODE_F22: 'f22',
    sdl2.SDL_SCANCODE_F23: 'f23',
    sdl2.SDL_SCANCODE_F24: 'f24',
    # letters
    sdl2.SDL_SCANCODE_A: 'a',
    sdl2.SDL_SCANCODE_B: 'b',
    sdl2.SDL_SCANCODE_C: 'c',
    sdl2.SDL_SCANCODE_D: 'd',
    sdl2.SDL_SCANCODE_E: 'e',
    sdl2.SDL_SCANCODE_F: 'f',
    sdl2.SDL_SCANCODE_G: 'g',
    sdl2.SDL_SCANCODE_H: 'h',
    sdl2.SDL_SCANCODE_I: 'i',
    sdl2.SDL_SCANCODE_J: 'j',
    sdl2.SDL_SCANCODE_K: 'k',
    sdl2.SDL_SCANCODE_L: 'l',
    sdl2.SDL_SCANCODE_M: 'm',
    sdl2.SDL_SCANCODE_N: 'n',
    sdl2.SDL_SCANCODE_O: 'o',
    sdl2.SDL_SCANCODE_P: 'p',
    sdl2.SDL_SCANCODE_Q: 'q',
    sdl2.SDL_SCANCODE_R: 'r',
    sdl2.SDL_SCANCODE_S: 's',
    sdl2.SDL_SCANCODE_T: 't',
    sdl2.SDL_SCANCODE_U: 'u',
    sdl2.SDL_SCANCODE_V: 'v',
    sdl2.SDL_SCANCODE_W: 'w',
    sdl2.SDL_SCANCODE_X: 'x',
    sdl2.SDL_SCANCODE_Y: 'y',
    sdl2.SDL_SCANCODE_Z: 'z',
    # symbols/operators
    sdl2.SDL_SCANCODE_APOSTROPHE: 'apostrophe',
    sdl2.SDL_SCANCODE_BACKSLASH: 'backslash',
    sdl2.SDL_SCANCODE_COMMA: 'comma',
    sdl2.SDL_SCANCODE_DECIMALSEPARATOR: 'decimal_separator',
    sdl2.SDL_SCANCODE_EQUALS: 'equals',
    sdl2.SDL_SCANCODE_GRAVE: 'grave',
    sdl2.SDL_SCANCODE_LEFTBRACKET: 'left_bracket',
    sdl2.SDL_SCANCODE_MINUS: 'minus',
    sdl2.SDL_SCANCODE_NONUSBACKSLASH: 'non_us_backslash',
    sdl2.SDL_SCANCODE_NONUSHASH: 'non_us_hash',
    sdl2.SDL_SCANCODE_PERIOD: 'period',
    sdl2.SDL_SCANCODE_RIGHTBRACKET: 'right_bracket',
    sdl2.SDL_SCANCODE_RSHIFT: 'right_shift',
    sdl2.SDL_SCANCODE_SEMICOLON: 'semicolon',
    sdl2.SDL_SCANCODE_SEPARATOR: 'separator',
    sdl2.SDL_SCANCODE_SLASH: 'slash',
    sdl2.SDL_SCANCODE_SPACE: 'space',
    sdl2.SDL_SCANCODE_TAB: 'tab',
    sdl2.SDL_SCANCODE_THOUSANDSSEPARATOR: 'thousands_separator',
    # actions
    sdl2.SDL_SCANCODE_AGAIN: 'again',
    sdl2.SDL_SCANCODE_ALTERASE: 'alt_erase',
    sdl2.SDL_SCANCODE_APP1: 'start_application_1',
    sdl2.SDL_SCANCODE_APP2: 'start_application_2',
    sdl2.SDL_SCANCODE_APPLICATION: 'context_menu',
    sdl2.SDL_SCANCODE_BACKSPACE: 'backspace',
    sdl2.SDL_SCANCODE_BRIGHTNESSDOWN: 'brightness_down',
    sdl2.SDL_SCANCODE_BRIGHTNESSUP: 'brightness_up',
    sdl2.SDL_SCANCODE_CALCULATOR: 'calculator',
    sdl2.SDL_SCANCODE_CANCEL: 'cancel',
    sdl2.SDL_SCANCODE_CAPSLOCK: 'capslock',
    sdl2.SDL_SCANCODE_CLEAR: 'clear',
    sdl2.SDL_SCANCODE_CLEARAGAIN: 'clear_again',
    sdl2.SDL_SCANCODE_COMPUTER: 'computer',
    sdl2.SDL_SCANCODE_COPY: 'copy',
    sdl2.SDL_SCANCODE_CRSEL: 'crsel',
    sdl2.SDL_SCANCODE_CURRENCYSUBUNIT: 'currency_sub_unit',
    sdl2.SDL_SCANCODE_CURRENCYUNIT: 'currency_unit',
    sdl2.SDL_SCANCODE_CUT: 'cut',
    sdl2.SDL_SCANCODE_DELETE: 'delete',
    sdl2.SDL_SCANCODE_DISPLAYSWITCH: 'display_switch',
    sdl2.SDL_SCANCODE_EJECT: 'eject',
    sdl2.SDL_SCANCODE_END: 'end',
    sdl2.SDL_SCANCODE_ESCAPE: 'escape',
    sdl2.SDL_SCANCODE_EXECUTE: 'execute',
    sdl2.SDL_SCANCODE_EXSEL: 'exsel',
    sdl2.SDL_SCANCODE_FIND: 'find',
    sdl2.SDL_SCANCODE_HELP: 'help',
    sdl2.SDL_SCANCODE_HOME: 'home',
    sdl2.SDL_SCANCODE_INSERT: 'insert',
    sdl2.SDL_SCANCODE_KBDILLUMDOWN: 'keyboard_illumination_down',
    sdl2.SDL_SCANCODE_KBDILLUMTOGGLE: 'keyboard_illumination_toggle',
    sdl2.SDL_SCANCODE_KBDILLUMUP: 'keyboard_illumination_up',
    sdl2.SDL_SCANCODE_LALT: 'left_alt',
    sdl2.SDL_SCANCODE_LCTRL: 'left_control',
    sdl2.SDL_SCANCODE_LGUI: 'left_special',
    sdl2.SDL_SCANCODE_LSHIFT: 'left_shift',
    sdl2.SDL_SCANCODE_MAIL: 'mail',
    sdl2.SDL_SCANCODE_MEDIASELECT: 'media_select',
    sdl2.SDL_SCANCODE_MENU: 'menu',
    sdl2.SDL_SCANCODE_MODE: 'mode',
    sdl2.SDL_SCANCODE_MUTE: 'mute',
    sdl2.SDL_SCANCODE_NUMLOCKCLEAR: 'numlock_clear',
    sdl2.SDL_SCANCODE_OPER: 'oper',
    sdl2.SDL_SCANCODE_OUT: 'out',
    sdl2.SDL_SCANCODE_PAGEDOWN: 'page_down',
    sdl2.SDL_SCANCODE_PAGEUP: 'page_up',
    sdl2.SDL_SCANCODE_PASTE: 'paste',
    sdl2.SDL_SCANCODE_PAUSE: 'pause',
    sdl2.SDL_SCANCODE_POWER: 'power',
    sdl2.SDL_SCANCODE_PRINTSCREEN: 'print_screen',
    sdl2.SDL_SCANCODE_PRIOR: 'prior',
    sdl2.SDL_SCANCODE_RALT: 'right_alt',
    sdl2.SDL_SCANCODE_RCTRL: 'right_control',
    sdl2.SDL_SCANCODE_RETURN: 'enter',
    sdl2.SDL_SCANCODE_RETURN2: 'enter_2',
    sdl2.SDL_SCANCODE_RGUI: 'right_special',
    sdl2.SDL_SCANCODE_SCROLLLOCK: 'scroll_lock',
    sdl2.SDL_SCANCODE_SELECT: 'select',
    sdl2.SDL_SCANCODE_SLEEP: 'sleep',
    sdl2.SDL_SCANCODE_STOP: 'stop',
    sdl2.SDL_SCANCODE_SYSREQ: 'system_request',
    sdl2.SDL_SCANCODE_UNDO: 'undo',
    sdl2.SDL_SCANCODE_VOLUMEDOWN: 'volume_down',
    sdl2.SDL_SCANCODE_VOLUMEUP: 'volume_up',
    sdl2.SDL_SCANCODE_WWW: 'www',
    # audio
    sdl2.SDL_SCANCODE_AUDIOFASTFORWARD: 'audio_fast_forward',
    sdl2.SDL_SCANCODE_AUDIOMUTE: 'audio_mute',
    sdl2.SDL_SCANCODE_AUDIONEXT: 'audio_next',
    sdl2.SDL_SCANCODE_AUDIOPLAY: 'audio_play',
    sdl2.SDL_SCANCODE_AUDIOPREV: 'audio_previous',
    sdl2.SDL_SCANCODE_AUDIOREWIND: 'audio_rewind',
    sdl2.SDL_SCANCODE_AUDIOSTOP: 'audio_stop',
    # ac
    sdl2.SDL_SCANCODE_AC_BACK: 'ac_back',
    sdl2.SDL_SCANCODE_AC_BOOKMARKS: 'ac_bookmarks',
    sdl2.SDL_SCANCODE_AC_FORWARD: 'ac_forward',
    sdl2.SDL_SCANCODE_AC_HOME: 'ac_home',
    sdl2.SDL_SCANCODE_AC_REFRESH: 'ac_refresh',
    sdl2.SDL_SCANCODE_AC_SEARCH: 'ac_search',
    sdl2.SDL_SCANCODE_AC_STOP: 'ac_stop',
    # arrows
    sdl2.SDL_SCANCODE_DOWN: 'down',
    sdl2.SDL_SCANCODE_LEFT: 'left',
    sdl2.SDL_SCANCODE_RIGHT: 'right',
    sdl2.SDL_SCANCODE_UP: 'up',
    # international
    sdl2.SDL_SCANCODE_INTERNATIONAL1: 'international_1',
    sdl2.SDL_SCANCODE_INTERNATIONAL2: 'international_2',
    sdl2.SDL_SCANCODE_INTERNATIONAL3: 'international_3',
    sdl2.SDL_SCANCODE_INTERNATIONAL4: 'international_4',
    sdl2.SDL_SCANCODE_INTERNATIONAL5: 'international_5',
    sdl2.SDL_SCANCODE_INTERNATIONAL6: 'international_6',
    sdl2.SDL_SCANCODE_INTERNATIONAL7: 'international_7',
    sdl2.SDL_SCANCODE_INTERNATIONAL8: 'international_8',
    sdl2.SDL_SCANCODE_INTERNATIONAL9: 'international_9',
    # numpad numbers
    sdl2.SDL_SCANCODE_KP_0: 'numpad_0',
    sdl2.SDL_SCANCODE_KP_00: 'numpad_00',
    sdl2.SDL_SCANCODE_KP_000: 'numpad_000',
    sdl2.SDL_SCANCODE_KP_1: 'numpad_1',
    sdl2.SDL_SCANCODE_KP_2: 'numpad_2',
    sdl2.SDL_SCANCODE_KP_3: 'numpad_3',
    sdl2.SDL_SCANCODE_KP_4: 'numpad_4',
    sdl2.SDL_SCANCODE_KP_5: 'numpad_5',
    sdl2.SDL_SCANCODE_KP_6: 'numpad_6',
    sdl2.SDL_SCANCODE_KP_7: 'numpad_7',
    sdl2.SDL_SCANCODE_KP_8: 'numpad_8',
    sdl2.SDL_SCANCODE_KP_9: 'numpad_9',
    # numpad letters
    sdl2.SDL_SCANCODE_KP_A: 'numpad_a',
    sdl2.SDL_SCANCODE_KP_B: 'numpad_b',
    sdl2.SDL_SCANCODE_KP_C: 'numpad_c',
    sdl2.SDL_SCANCODE_KP_D: 'numpad_d',
    sdl2.SDL_SCANCODE_KP_E: 'numpad_e',
    sdl2.SDL_SCANCODE_KP_F: 'numpad_f',
    # numpad symbols/operators
    sdl2.SDL_SCANCODE_KP_AMPERSAND: 'numpad_ampersand',
    sdl2.SDL_SCANCODE_KP_AT: 'numpad_at',
    sdl2.SDL_SCANCODE_KP_COLON: 'numpad_colon',
    sdl2.SDL_SCANCODE_KP_COMMA: 'numpad_comma',
    sdl2.SDL_SCANCODE_KP_DBLAMPERSAND: 'numpad_and',
    sdl2.SDL_SCANCODE_KP_DBLVERTICALBAR: 'numpad_or',
    sdl2.SDL_SCANCODE_KP_DECIMAL: 'numpad_decimal',
    sdl2.SDL_SCANCODE_KP_DIVIDE: 'numpad_divide',
    sdl2.SDL_SCANCODE_KP_ENTER: 'numpad_enter',
    sdl2.SDL_SCANCODE_KP_EQUALS: 'numpad_equals',
    sdl2.SDL_SCANCODE_KP_EQUALSAS400: 'numpad_as400_equals',
    sdl2.SDL_SCANCODE_KP_EXCLAM: 'numpad_bang',
    sdl2.SDL_SCANCODE_KP_GREATER: 'numpad_greater',
    sdl2.SDL_SCANCODE_KP_HASH: 'numpad_hash',
    sdl2.SDL_SCANCODE_KP_LEFTBRACE: 'numpad_left_brace',
    sdl2.SDL_SCANCODE_KP_LEFTPAREN: 'numpad_left_parenthesis',
    sdl2.SDL_SCANCODE_KP_LESS: 'numpad_less',
    sdl2.SDL_SCANCODE_KP_MINUS: 'numpad_minus',
    sdl2.SDL_SCANCODE_KP_MULTIPLY: 'numpad_multiply',
    sdl2.SDL_SCANCODE_KP_PERCENT: 'numpad_percent',
    sdl2.SDL_SCANCODE_KP_PERIOD: 'numpad_period',
    sdl2.SDL_SCANCODE_KP_PLUS: 'numpad_plus',
    sdl2.SDL_SCANCODE_KP_PLUSMINUS: 'numpad_plus_minus',
    sdl2.SDL_SCANCODE_KP_POWER: 'numpad_power',
    sdl2.SDL_SCANCODE_KP_RIGHTBRACE: 'numpad_right_brace',
    sdl2.SDL_SCANCODE_KP_RIGHTPAREN: 'numpad_right_parenthesis',
    sdl2.SDL_SCANCODE_KP_SPACE: 'numpad_space',
    sdl2.SDL_SCANCODE_KP_TAB: 'numpad_tab',
    sdl2.SDL_SCANCODE_KP_VERTICALBAR: 'numpad_pipe',
    sdl2.SDL_SCANCODE_KP_XOR: 'numpad_xor',
    # numpad actions
    sdl2.SDL_SCANCODE_KP_BACKSPACE: 'numpad_backspace',
    sdl2.SDL_SCANCODE_KP_BINARY: 'numpad_binary',
    sdl2.SDL_SCANCODE_KP_CLEAR: 'numpad_clear',
    sdl2.SDL_SCANCODE_KP_CLEARENTRY: 'numpad_clear_entry',
    sdl2.SDL_SCANCODE_KP_HEXADECIMAL: 'numpad_hexadecimal',
    sdl2.SDL_SCANCODE_KP_OCTAL: 'numpad_octal',
    # memory
    sdl2.SDL_SCANCODE_KP_MEMADD: 'numpad_memory_add',
    sdl2.SDL_SCANCODE_KP_MEMCLEAR: 'numpad_memory_clear',
    sdl2.SDL_SCANCODE_KP_MEMDIVIDE: 'numpad_memory_divide',
    sdl2.SDL_SCANCODE_KP_MEMMULTIPLY: 'numpad_memory_multiply',
    sdl2.SDL_SCANCODE_KP_MEMRECALL: 'numpad_memory_recall',
    sdl2.SDL_SCANCODE_KP_MEMSTORE: 'numpad_memory_store',
    sdl2.SDL_SCANCODE_KP_MEMSUBTRACT: 'numpad_memory_subtract',
    # language
    sdl2.SDL_SCANCODE_LANG1: 'language_1',
    sdl2.SDL_SCANCODE_LANG2: 'language_2',
    sdl2.SDL_SCANCODE_LANG3: 'language_3',
    sdl2.SDL_SCANCODE_LANG4: 'language_4',
    sdl2.SDL_SCANCODE_LANG5: 'language_5',
    sdl2.SDL_SCANCODE_LANG6: 'language_6',
    sdl2.SDL_SCANCODE_LANG7: 'language_7',
    sdl2.SDL_SCANCODE_LANG8: 'language_8',
    sdl2.SDL_SCANCODE_LANG9: 'language_9',
}

key_names: Final = set(sdl_scancode_to_gamut_key_name.values())
assert len(key_names) == len(sdl_scancode_to_gamut_key_name)

special_key_name: Final = (
    '⊞ Win' if platform.system() == 'Windows' else
    '⌘ Command' if platform.system() == 'Darwin' else
    'Command'
)

sdl_keycode_to_gamut_key_name: Final = {
    # numbers
    sdl2.SDLK_0: '0',
    sdl2.SDLK_1: '1',
    sdl2.SDLK_2: '2',
    sdl2.SDLK_3: '3',
    sdl2.SDLK_4: '4',
    sdl2.SDLK_5: '5',
    sdl2.SDLK_6: '6',
    sdl2.SDLK_7: '7',
    sdl2.SDLK_8: '8',
    sdl2.SDLK_9: '9',
    # browser
    sdl2.SDLK_AC_BACK: 'Browser Back',
    sdl2.SDLK_AC_BOOKMARKS: 'Browser Bookmarks',
    sdl2.SDLK_AC_FORWARD: 'Browser Forward',
    sdl2.SDLK_AC_HOME: 'Browser Home',
    sdl2.SDLK_AC_REFRESH: 'Browser Refresh',
    sdl2.SDLK_AC_SEARCH: 'Browser Search',
    sdl2.SDLK_AC_STOP: 'Browser Stop',
    # actions
    sdl2.SDLK_AGAIN: 'Again',
    sdl2.SDLK_ALTERASE: 'Alt Erase',
    sdl2.SDLK_APP1: 'App 1',
    sdl2.SDLK_APP2: 'App 2',
    sdl2.SDLK_APPLICATION: 'Application',
    sdl2.SDLK_BACKSPACE: 'Backspace',
    sdl2.SDLK_BRIGHTNESSDOWN: 'Brightness Down',
    sdl2.SDLK_BRIGHTNESSUP: 'Brightness Up',
    sdl2.SDLK_CALCULATOR: 'Calculator',
    sdl2.SDLK_CANCEL: 'Cancel',
    sdl2.SDLK_CAPSLOCK: 'Capslock',
    sdl2.SDLK_CLEAR: 'Clear',
    sdl2.SDLK_CLEARAGAIN: 'Clear Again',
    sdl2.SDLK_COMPUTER: 'Computer',
    sdl2.SDLK_COPY: 'Copy',
    sdl2.SDLK_CRSEL: 'Cr Sel',
    sdl2.SDLK_CURRENCYSUBUNIT: 'Currency Sub-Unit',
    sdl2.SDLK_CURRENCYUNIT: 'Currency Unit',
    sdl2.SDLK_CUT: 'Cut',
    sdl2.SDLK_DELETE: 'Delete',
    sdl2.SDLK_DISPLAYSWITCH: 'Switch Display',
    sdl2.SDLK_EJECT: 'Eject',
    sdl2.SDLK_END: 'End',
    sdl2.SDLK_ESCAPE: 'Escape',
    sdl2.SDLK_EXECUTE: 'Execute',
    sdl2.SDLK_EXSEL: 'Ex Sel',
    sdl2.SDLK_FIND: 'Find',
    sdl2.SDLK_HELP: 'Help',
    sdl2.SDLK_HOME: 'Home',
    sdl2.SDLK_INSERT: 'Insert',
    sdl2.SDLK_KBDILLUMDOWN: 'Keyboard Illumination Down',
    sdl2.SDLK_KBDILLUMTOGGLE: 'Keyboard Illumination Toggle',
    sdl2.SDLK_KBDILLUMUP: 'Keyboard Illumination Up',
    sdl2.SDLK_LALT: 'Left Alt',
    sdl2.SDLK_LCTRL: 'Left Ctrl',
    sdl2.SDLK_LGUI: f'Left {special_key_name}',
    sdl2.SDLK_LSHIFT: 'Left Shift',
    sdl2.SDLK_MAIL: 'Mail',
    sdl2.SDLK_MEDIASELECT: 'Media Select',
    sdl2.SDLK_MENU: 'Menu',
    sdl2.SDLK_MODE: 'Mode',
    sdl2.SDLK_MUTE: 'Mute',
    sdl2.SDLK_NUMLOCKCLEAR: 'Num Lock Clear',
    sdl2.SDLK_OPER: 'Oper',
    sdl2.SDLK_OUT: 'Out',
    sdl2.SDLK_PAGEDOWN: 'Page Down',
    sdl2.SDLK_PAGEUP: 'Page Up',
    sdl2.SDLK_PASTE: 'Paste',
    sdl2.SDLK_PAUSE: 'Pause',
    sdl2.SDLK_POWER: 'Power',
    sdl2.SDLK_PRINTSCREEN: 'Print Screen',
    sdl2.SDLK_PRIOR: 'Prior',
    sdl2.SDLK_RALT: 'Right Alt',
    sdl2.SDLK_RCTRL: 'Right Ctrl',
    sdl2.SDLK_RETURN: 'Enter',
    sdl2.SDLK_RETURN2: 'Return 2',
    sdl2.SDLK_RGUI: f'Right {special_key_name}',
    sdl2.SDLK_RSHIFT: 'Right Shift',
    sdl2.SDLK_SCROLLLOCK: 'Scroll Lock',
    sdl2.SDLK_SELECT: 'Select',
    sdl2.SDLK_SLEEP: 'Sleep',
    sdl2.SDLK_SPACE: 'Space',
    sdl2.SDLK_STOP: 'Stop',
    sdl2.SDLK_SYSREQ: 'Sys Req',
    sdl2.SDLK_TAB: 'Tab',
    sdl2.SDLK_THOUSANDSSEPARATOR: 'Thousands Separator',
    sdl2.SDLK_UNDO: 'Undo',
    sdl2.SDLK_VOLUMEDOWN: 'Volume Down',
    sdl2.SDLK_VOLUMEUP: 'Volume Up',
    sdl2.SDLK_WWW: 'www',
    # symbols/operators
    sdl2.SDLK_AMPERSAND: '&',
    sdl2.SDLK_ASTERISK: '*',
    sdl2.SDLK_AT: '@',
    sdl2.SDLK_BACKQUOTE: '`',
    sdl2.SDLK_BACKSLASH: '\\',
    sdl2.SDLK_CARET: '^',
    sdl2.SDLK_COLON: ':',
    sdl2.SDLK_COMMA: ',',
    sdl2.SDLK_DECIMALSEPARATOR: 'Decimal Separator',
    sdl2.SDLK_DOLLAR: '$',
    sdl2.SDLK_EQUALS: '=',
    sdl2.SDLK_EXCLAIM: '!',
    sdl2.SDLK_GREATER: '>',
    sdl2.SDLK_HASH: '#',
    sdl2.SDLK_LEFTBRACKET: '[',
    sdl2.SDLK_LEFTPAREN: '(',
    sdl2.SDLK_LESS: '<',
    sdl2.SDLK_MINUS: '-',
    sdl2.SDLK_PERCENT: '%',
    sdl2.SDLK_PERIOD: '.',
    sdl2.SDLK_PLUS: '+',
    sdl2.SDLK_QUESTION: '?',
    sdl2.SDLK_QUOTE: '\'',
    sdl2.SDLK_QUOTEDBL: '"',
    sdl2.SDLK_RIGHTBRACKET: ']',
    sdl2.SDLK_RIGHTPAREN: ')',
    sdl2.SDLK_SEMICOLON: ';',
    sdl2.SDLK_SEPARATOR: 'Separator',
    sdl2.SDLK_SLASH: '/',
    sdl2.SDLK_UNDERSCORE: '_',
    # audio
    sdl2.SDLK_AUDIOFASTFORWARD: 'Fast Forward Song',
    sdl2.SDLK_AUDIOMUTE: 'Mute Song',
    sdl2.SDLK_AUDIONEXT: 'Next Song',
    sdl2.SDLK_AUDIOPLAY: 'Play Song',
    sdl2.SDLK_AUDIOPREV: 'Previous Song',
    sdl2.SDLK_AUDIOREWIND: 'Rewind Song',
    sdl2.SDLK_AUDIOSTOP: 'Stop Song',
    # arrows
    sdl2.SDLK_DOWN: 'Down',
    sdl2.SDLK_LEFT: 'Left',
    sdl2.SDLK_RIGHT: 'Right',
    sdl2.SDLK_UP: 'Up',
    # function
    sdl2.SDLK_F1: 'F1',
    sdl2.SDLK_F2: 'F2',
    sdl2.SDLK_F3: 'F3',
    sdl2.SDLK_F4: 'F4',
    sdl2.SDLK_F5: 'F5',
    sdl2.SDLK_F6: 'F6',
    sdl2.SDLK_F7: 'F7',
    sdl2.SDLK_F8: 'F8',
    sdl2.SDLK_F9: 'F9',
    sdl2.SDLK_F10: 'F10',
    sdl2.SDLK_F11: 'F11',
    sdl2.SDLK_F12: 'F12',
    sdl2.SDLK_F13: 'F13',
    sdl2.SDLK_F14: 'F14',
    sdl2.SDLK_F15: 'F15',
    sdl2.SDLK_F16: 'F16',
    sdl2.SDLK_F17: 'F17',
    sdl2.SDLK_F18: 'F18',
    sdl2.SDLK_F19: 'F19',
    sdl2.SDLK_F20: 'F20',
    sdl2.SDLK_F21: 'F21',
    sdl2.SDLK_F22: 'F22',
    sdl2.SDLK_F23: 'F23',
    sdl2.SDLK_F24: 'F24',
    # numpad symbols/operators
    sdl2.SDLK_KP_0: 'Numpad 0',
    sdl2.SDLK_KP_00: 'Numpad 00',
    sdl2.SDLK_KP_000: 'Numpad 000',
    sdl2.SDLK_KP_1: 'Numpad 1',
    sdl2.SDLK_KP_2: 'Numpad 2',
    sdl2.SDLK_KP_3: 'Numpad 3',
    sdl2.SDLK_KP_4: 'Numpad 4',
    sdl2.SDLK_KP_5: 'Numpad 5',
    sdl2.SDLK_KP_6: 'Numpad 6',
    sdl2.SDLK_KP_7: 'Numpad 7',
    sdl2.SDLK_KP_8: 'Numpad 8',
    sdl2.SDLK_KP_9: 'Numpad 9',
    # numpad letters
    sdl2.SDLK_KP_A: 'Numpad A',
    sdl2.SDLK_KP_B: 'Numpad B',
    sdl2.SDLK_KP_C: 'Numpad C',
    sdl2.SDLK_KP_D: 'Numpad D',
    sdl2.SDLK_KP_E: 'Numpad E',
    sdl2.SDLK_KP_F: 'Numpad F',
    # numpad operators/symbols
    sdl2.SDLK_KP_AMPERSAND: 'Numpad &',
    sdl2.SDLK_KP_AT: 'Numpad @',
    sdl2.SDLK_KP_COLON: 'Numpad :',
    sdl2.SDLK_KP_COMMA: 'Numpad ,',
    sdl2.SDLK_KP_DBLAMPERSAND: 'Numpad &&',
    sdl2.SDLK_KP_DBLVERTICALBAR: 'Numpad ||',
    sdl2.SDLK_KP_DECIMAL: 'Numpad Decimal',
    sdl2.SDLK_KP_DIVIDE: 'Numpad /',
    sdl2.SDLK_KP_EQUALS: 'Numpad =',
    sdl2.SDLK_KP_EQUALSAS400: 'Numpad AS400 =',
    sdl2.SDLK_KP_EXCLAM: 'Numpad !',
    sdl2.SDLK_KP_GREATER: 'Numpad >',
    sdl2.SDLK_KP_HASH: 'Numpad #',
    sdl2.SDLK_KP_LEFTBRACE: 'Numpad {',
    sdl2.SDLK_KP_LEFTPAREN: 'Numpad (',
    sdl2.SDLK_KP_LESS: 'Numpad <',
    sdl2.SDLK_KP_MINUS: 'Numpad -',
    sdl2.SDLK_KP_MULTIPLY: 'Numpad *',
    sdl2.SDLK_KP_PERCENT: 'Numpad %',
    sdl2.SDLK_KP_PERIOD: 'Numpad .',
    sdl2.SDLK_KP_PLUS: 'Numpad +',
    sdl2.SDLK_KP_PLUSMINUS: 'Numpad ±',
    sdl2.SDLK_KP_POWER: 'Numpad ^',
    sdl2.SDLK_KP_RIGHTBRACE: 'Numpad }',
    sdl2.SDLK_KP_RIGHTPAREN: 'Numpad )',
    sdl2.SDLK_KP_SPACE: 'Numpad Space',
    sdl2.SDLK_KP_TAB: 'Numpad Tab',
    sdl2.SDLK_KP_VERTICALBAR: 'Numpad |',
    sdl2.SDLK_KP_XOR: 'Numpad ⊻',
    # numpad actions
    sdl2.SDLK_KP_BACKSPACE: 'Numpad Backspace',
    sdl2.SDLK_KP_BINARY: 'Numpad Binary',
    sdl2.SDLK_KP_CLEAR: 'Numpad Clear',
    sdl2.SDLK_KP_CLEARENTRY: 'Numpad Clear Entry',
    sdl2.SDLK_KP_ENTER: 'Numpad Enter',
    sdl2.SDLK_KP_HEXADECIMAL: 'Numpad Hexadecimal',
    sdl2.SDLK_KP_OCTAL: 'Numpad Octal',
    # numpad memory
    sdl2.SDLK_KP_MEMADD: 'Numpad MemAdd',
    sdl2.SDLK_KP_MEMCLEAR: 'Numpad MemClear',
    sdl2.SDLK_KP_MEMDIVIDE: 'Numpad MemDivide',
    sdl2.SDLK_KP_MEMMULTIPLY: 'Numpad MemMultiply',
    sdl2.SDLK_KP_MEMRECALL: 'Numpad MemRecall',
    sdl2.SDLK_KP_MEMSTORE: 'Numpad MemStore',
    sdl2.SDLK_KP_MEMSUBTRACT: 'Numpad MemSubtract',
    # letters
    sdl2.SDLK_a: 'A',
    sdl2.SDLK_b: 'B',
    sdl2.SDLK_c: 'C',
    sdl2.SDLK_d: 'D',
    sdl2.SDLK_e: 'E',
    sdl2.SDLK_f: 'F',
    sdl2.SDLK_g: 'G',
    sdl2.SDLK_h: 'H',
    sdl2.SDLK_i: 'I',
    sdl2.SDLK_j: 'J',
    sdl2.SDLK_k: 'K',
    sdl2.SDLK_l: 'L',
    sdl2.SDLK_m: 'M',
    sdl2.SDLK_n: 'N',
    sdl2.SDLK_o: 'O',
    sdl2.SDLK_p: 'P',
    sdl2.SDLK_q: 'Q',
    sdl2.SDLK_r: 'R',
    sdl2.SDLK_s: 'S',
    sdl2.SDLK_t: 'T',
    sdl2.SDLK_u: 'U',
    sdl2.SDLK_v: 'V',
    sdl2.SDLK_w: 'W',
    sdl2.SDLK_x: 'X',
    sdl2.SDLK_y: 'Y',
    sdl2.SDLK_z: 'Z',
}


class KeyboardEvent(PeripheralEvent, peripheral=...):
    peripheral: Keyboard

    @property
    def keyboard(self) -> Keyboard:
        return self.peripheral


class KeyboardKeyEvent(KeyboardEvent, peripheral=..., key=...):
    key: KeyboardKey
    is_pressed: bool


class KeyboardKeyPressed(KeyboardKeyEvent,
    peripheral=..., key=..., is_pressed=True
):
    pass


class KeyboardKeyReleased(KeyboardKeyEvent,
    peripheral=..., key=..., is_pressed=False
):
    pass


class KeyboardConnected(KeyboardEvent, PeripheralConnected, peripheral=...):
    pass


class KeyboardDisconnected(KeyboardEvent, PeripheralDisconnected,
    peripheral=...
):
    pass


class KeyboardFocused(KeyboardEvent, peripheral=...):
    window: Window


class KeyboardLostFocus(KeyboardEvent, peripheral=...):
    pass


class BaseKeyboardKey:

    def __init_subclass__(cls, keyboard: Optional[Keyboard] = None):
        super().__init_subclass__()
        for key_name in key_names:
            setattr(cls, key_name, cls(key_name, keyboard=keyboard))

    def __init__(self, name: str, keyboard: Optional[Keyboard] = None):
        self._name = name
        self._keyboard: Optional[ref[Keyboard]] = (
            ref(keyboard) if keyboard else None
        )

    def __repr__(self) -> str:
        identifier = repr(self._name)
        if self._keyboard:
            keyboard = self._keyboard()
            if keyboard:
                identifier = f'{identifier} for {keyboard!r}'
        return f'<gamut.peripheral.KeyboardKey {identifier}>'

    @property
    def name(self) -> str:
        return self._name


class KeyboardKey(BaseKeyboardKey):

    zero: ClassVar[KeyboardKey]
    one: ClassVar[KeyboardKey]
    two: ClassVar[KeyboardKey]
    three: ClassVar[KeyboardKey]
    four: ClassVar[KeyboardKey]
    five: ClassVar[KeyboardKey]
    six: ClassVar[KeyboardKey]
    seven: ClassVar[KeyboardKey]
    eight: ClassVar[KeyboardKey]
    nine: ClassVar[KeyboardKey]
    f1: ClassVar[KeyboardKey]
    f2: ClassVar[KeyboardKey]
    f3: ClassVar[KeyboardKey]
    f4: ClassVar[KeyboardKey]
    f5: ClassVar[KeyboardKey]
    f6: ClassVar[KeyboardKey]
    f7: ClassVar[KeyboardKey]
    f8: ClassVar[KeyboardKey]
    f9: ClassVar[KeyboardKey]
    f10: ClassVar[KeyboardKey]
    f11: ClassVar[KeyboardKey]
    f12: ClassVar[KeyboardKey]
    f13: ClassVar[KeyboardKey]
    f14: ClassVar[KeyboardKey]
    f15: ClassVar[KeyboardKey]
    f16: ClassVar[KeyboardKey]
    f17: ClassVar[KeyboardKey]
    f18: ClassVar[KeyboardKey]
    f19: ClassVar[KeyboardKey]
    f20: ClassVar[KeyboardKey]
    f21: ClassVar[KeyboardKey]
    f22: ClassVar[KeyboardKey]
    f23: ClassVar[KeyboardKey]
    f24: ClassVar[KeyboardKey]
    a: ClassVar[KeyboardKey]
    b: ClassVar[KeyboardKey]
    c: ClassVar[KeyboardKey]
    d: ClassVar[KeyboardKey]
    e: ClassVar[KeyboardKey]
    f: ClassVar[KeyboardKey]
    g: ClassVar[KeyboardKey]
    h: ClassVar[KeyboardKey]
    i: ClassVar[KeyboardKey]
    j: ClassVar[KeyboardKey]
    k: ClassVar[KeyboardKey]
    l: ClassVar[KeyboardKey]
    m: ClassVar[KeyboardKey]
    n: ClassVar[KeyboardKey]
    o: ClassVar[KeyboardKey]
    p: ClassVar[KeyboardKey]
    q: ClassVar[KeyboardKey]
    r: ClassVar[KeyboardKey]
    s: ClassVar[KeyboardKey]
    t: ClassVar[KeyboardKey]
    u: ClassVar[KeyboardKey]
    v: ClassVar[KeyboardKey]
    w: ClassVar[KeyboardKey]
    x: ClassVar[KeyboardKey]
    y: ClassVar[KeyboardKey]
    z: ClassVar[KeyboardKey]
    apostrophe: ClassVar[KeyboardKey]
    backslash: ClassVar[KeyboardKey]
    comma: ClassVar[KeyboardKey]
    decimal_separator: ClassVar[KeyboardKey]
    equals: ClassVar[KeyboardKey]
    grave: ClassVar[KeyboardKey]
    left_bracket: ClassVar[KeyboardKey]
    minus: ClassVar[KeyboardKey]
    non_us_backslash: ClassVar[KeyboardKey]
    non_us_hash: ClassVar[KeyboardKey]
    period: ClassVar[KeyboardKey]
    right_bracket: ClassVar[KeyboardKey]
    right_shift: ClassVar[KeyboardKey]
    semicolon: ClassVar[KeyboardKey]
    separator: ClassVar[KeyboardKey]
    slash: ClassVar[KeyboardKey]
    space: ClassVar[KeyboardKey]
    tab: ClassVar[KeyboardKey]
    thousands_separator: ClassVar[KeyboardKey]
    again: ClassVar[KeyboardKey]
    alt_erase: ClassVar[KeyboardKey]
    start_application_1: ClassVar[KeyboardKey]
    start_application_2: ClassVar[KeyboardKey]
    context_menu: ClassVar[KeyboardKey]
    backspace: ClassVar[KeyboardKey]
    brightness_down: ClassVar[KeyboardKey]
    brightness_up: ClassVar[KeyboardKey]
    calculator: ClassVar[KeyboardKey]
    cancel: ClassVar[KeyboardKey]
    capslock: ClassVar[KeyboardKey]
    clear: ClassVar[KeyboardKey]
    clear_again: ClassVar[KeyboardKey]
    computer: ClassVar[KeyboardKey]
    copy: ClassVar[KeyboardKey]
    crsel: ClassVar[KeyboardKey]
    currency_sub_unit: ClassVar[KeyboardKey]
    currency_unit: ClassVar[KeyboardKey]
    cut: ClassVar[KeyboardKey]
    delete: ClassVar[KeyboardKey]
    display_switch: ClassVar[KeyboardKey]
    eject: ClassVar[KeyboardKey]
    end: ClassVar[KeyboardKey]
    escape: ClassVar[KeyboardKey]
    execute: ClassVar[KeyboardKey]
    exsel: ClassVar[KeyboardKey]
    find: ClassVar[KeyboardKey]
    help: ClassVar[KeyboardKey]
    home: ClassVar[KeyboardKey]
    insert: ClassVar[KeyboardKey]
    keyboard_illumination_down: ClassVar[KeyboardKey]
    keyboard_illumination_toggle: ClassVar[KeyboardKey]
    keyboard_illumination_up: ClassVar[KeyboardKey]
    left_alt: ClassVar[KeyboardKey]
    left_control: ClassVar[KeyboardKey]
    left_special: ClassVar[KeyboardKey]
    left_shift: ClassVar[KeyboardKey]
    mail: ClassVar[KeyboardKey]
    media_select: ClassVar[KeyboardKey]
    menu: ClassVar[KeyboardKey]
    mode: ClassVar[KeyboardKey]
    mute: ClassVar[KeyboardKey]
    numlock_clear: ClassVar[KeyboardKey]
    oper: ClassVar[KeyboardKey]
    out: ClassVar[KeyboardKey]
    page_down: ClassVar[KeyboardKey]
    page_up: ClassVar[KeyboardKey]
    paste: ClassVar[KeyboardKey]
    pause: ClassVar[KeyboardKey]
    power: ClassVar[KeyboardKey]
    print_screen: ClassVar[KeyboardKey]
    prior: ClassVar[KeyboardKey]
    right_alt: ClassVar[KeyboardKey]
    right_control: ClassVar[KeyboardKey]
    enter: ClassVar[KeyboardKey]
    enter_2: ClassVar[KeyboardKey]
    right_special: ClassVar[KeyboardKey]
    scroll_lock: ClassVar[KeyboardKey]
    select: ClassVar[KeyboardKey]
    sleep: ClassVar[KeyboardKey]
    stop: ClassVar[KeyboardKey]
    system_request: ClassVar[KeyboardKey]
    undo: ClassVar[KeyboardKey]
    volume_down: ClassVar[KeyboardKey]
    volume_up: ClassVar[KeyboardKey]
    www: ClassVar[KeyboardKey]
    audio_fast_forward: ClassVar[KeyboardKey]
    audio_mute: ClassVar[KeyboardKey]
    audio_next: ClassVar[KeyboardKey]
    audio_play: ClassVar[KeyboardKey]
    audio_previous: ClassVar[KeyboardKey]
    audio_rewind: ClassVar[KeyboardKey]
    audio_stop: ClassVar[KeyboardKey]
    ac_back: ClassVar[KeyboardKey]
    ac_bookmarks: ClassVar[KeyboardKey]
    ac_forward: ClassVar[KeyboardKey]
    ac_home: ClassVar[KeyboardKey]
    ac_refresh: ClassVar[KeyboardKey]
    ac_search: ClassVar[KeyboardKey]
    ac_stop: ClassVar[KeyboardKey]
    down: ClassVar[KeyboardKey]
    left: ClassVar[KeyboardKey]
    right: ClassVar[KeyboardKey]
    up: ClassVar[KeyboardKey]
    international_1: ClassVar[KeyboardKey]
    international_2: ClassVar[KeyboardKey]
    international_3: ClassVar[KeyboardKey]
    international_4: ClassVar[KeyboardKey]
    international_5: ClassVar[KeyboardKey]
    international_6: ClassVar[KeyboardKey]
    international_7: ClassVar[KeyboardKey]
    international_8: ClassVar[KeyboardKey]
    international_9: ClassVar[KeyboardKey]
    numpad_0: ClassVar[KeyboardKey]
    numpad_00: ClassVar[KeyboardKey]
    numpad_000: ClassVar[KeyboardKey]
    numpad_1: ClassVar[KeyboardKey]
    numpad_2: ClassVar[KeyboardKey]
    numpad_3: ClassVar[KeyboardKey]
    numpad_4: ClassVar[KeyboardKey]
    numpad_5: ClassVar[KeyboardKey]
    numpad_6: ClassVar[KeyboardKey]
    numpad_7: ClassVar[KeyboardKey]
    numpad_8: ClassVar[KeyboardKey]
    numpad_9: ClassVar[KeyboardKey]
    numpad_a: ClassVar[KeyboardKey]
    numpad_b: ClassVar[KeyboardKey]
    numpad_c: ClassVar[KeyboardKey]
    numpad_d: ClassVar[KeyboardKey]
    numpad_e: ClassVar[KeyboardKey]
    numpad_f: ClassVar[KeyboardKey]
    numpad_ampersand: ClassVar[KeyboardKey]
    numpad_at: ClassVar[KeyboardKey]
    numpad_colon: ClassVar[KeyboardKey]
    numpad_comma: ClassVar[KeyboardKey]
    numpad_and: ClassVar[KeyboardKey]
    numpad_or: ClassVar[KeyboardKey]
    numpad_decimal: ClassVar[KeyboardKey]
    numpad_divide: ClassVar[KeyboardKey]
    numpad_enter: ClassVar[KeyboardKey]
    numpad_equals: ClassVar[KeyboardKey]
    numpad_as400_equals: ClassVar[KeyboardKey]
    numpad_bang: ClassVar[KeyboardKey]
    numpad_greater: ClassVar[KeyboardKey]
    numpad_hash: ClassVar[KeyboardKey]
    numpad_left_brace: ClassVar[KeyboardKey]
    numpad_left_parenthesis: ClassVar[KeyboardKey]
    numpad_less: ClassVar[KeyboardKey]
    numpad_minus: ClassVar[KeyboardKey]
    numpad_multiply: ClassVar[KeyboardKey]
    numpad_percent: ClassVar[KeyboardKey]
    numpad_period: ClassVar[KeyboardKey]
    numpad_plus: ClassVar[KeyboardKey]
    numpad_plus_minus: ClassVar[KeyboardKey]
    numpad_power: ClassVar[KeyboardKey]
    numpad_right_brace: ClassVar[KeyboardKey]
    numpad_right_parenthesis: ClassVar[KeyboardKey]
    numpad_space: ClassVar[KeyboardKey]
    numpad_tab: ClassVar[KeyboardKey]
    numpad_pipe: ClassVar[KeyboardKey]
    numpad_xor: ClassVar[KeyboardKey]
    numpad_backspace: ClassVar[KeyboardKey]
    numpad_binary: ClassVar[KeyboardKey]
    numpad_clear: ClassVar[KeyboardKey]
    numpad_clear_entry: ClassVar[KeyboardKey]
    numpad_hexadecimal: ClassVar[KeyboardKey]
    numpad_octal: ClassVar[KeyboardKey]
    numpad_memory_add: ClassVar[KeyboardKey]
    numpad_memory_clear: ClassVar[KeyboardKey]
    numpad_memory_divide: ClassVar[KeyboardKey]
    numpad_memory_multiply: ClassVar[KeyboardKey]
    numpad_memory_recall: ClassVar[KeyboardKey]
    numpad_memory_store: ClassVar[KeyboardKey]
    numpad_memory_subtract: ClassVar[KeyboardKey]
    language_1: ClassVar[KeyboardKey]
    language_2: ClassVar[KeyboardKey]
    language_3: ClassVar[KeyboardKey]
    language_4: ClassVar[KeyboardKey]
    language_5: ClassVar[KeyboardKey]
    language_6: ClassVar[KeyboardKey]
    language_7: ClassVar[KeyboardKey]
    language_8: ClassVar[KeyboardKey]
    language_9: ClassVar[KeyboardKey]

    Event: type[KeyboardKeyEvent]
    Pressed: type[KeyboardKeyPressed]
    Released: type[KeyboardKeyReleased]

    def __init__(self, name: str, keyboard: Optional[Keyboard] = None):
        super().__init__(name, keyboard=keyboard)
        if keyboard:
            class EventWithKeyboard( # type: ignore
                KeyboardKeyEvent,
                keyboard.Event, # type: ignore
                key=self
            ):
                pass
            self.Event = EventWithKeyboard
            class PressedWithKeyboard( # type: ignore
                KeyboardKeyPressed,
                EventWithKeyboard
            ):
                pass
            self.Pressed = PressedWithKeyboard
            class ReleasedWithKeyboard( # type: ignore
                KeyboardKeyReleased,
                EventWithKeyboard
            ):
                pass
            self.Released = ReleasedWithKeyboard
        else:
            class EventNoKeyboard(KeyboardKeyEvent,
                peripheral=..., key=self
            ):
                pass
            self.Event = EventNoKeyboard
            class PressedNoKeyboard(KeyboardKeyPressed, EventNoKeyboard,
                peripheral=...
            ):
                pass
            self.Pressed = PressedNoKeyboard
            class ReleasedNoKeyboard(KeyboardKeyReleased, EventNoKeyboard,
                peripheral=...
            ):
                pass
            self.Released = ReleasedNoKeyboard


class PressableKeyboardKey(KeyboardKey):

    zero: ClassVar[PressableKeyboardKey]
    one: ClassVar[PressableKeyboardKey]
    two: ClassVar[PressableKeyboardKey]
    three: ClassVar[PressableKeyboardKey]
    four: ClassVar[PressableKeyboardKey]
    five: ClassVar[PressableKeyboardKey]
    six: ClassVar[PressableKeyboardKey]
    seven: ClassVar[PressableKeyboardKey]
    eight: ClassVar[PressableKeyboardKey]
    nine: ClassVar[PressableKeyboardKey]
    f1: ClassVar[PressableKeyboardKey]
    f2: ClassVar[PressableKeyboardKey]
    f3: ClassVar[PressableKeyboardKey]
    f4: ClassVar[PressableKeyboardKey]
    f5: ClassVar[PressableKeyboardKey]
    f6: ClassVar[PressableKeyboardKey]
    f7: ClassVar[PressableKeyboardKey]
    f8: ClassVar[PressableKeyboardKey]
    f9: ClassVar[PressableKeyboardKey]
    f10: ClassVar[PressableKeyboardKey]
    f11: ClassVar[PressableKeyboardKey]
    f12: ClassVar[PressableKeyboardKey]
    f13: ClassVar[PressableKeyboardKey]
    f14: ClassVar[PressableKeyboardKey]
    f15: ClassVar[PressableKeyboardKey]
    f16: ClassVar[PressableKeyboardKey]
    f17: ClassVar[PressableKeyboardKey]
    f18: ClassVar[PressableKeyboardKey]
    f19: ClassVar[PressableKeyboardKey]
    f20: ClassVar[PressableKeyboardKey]
    f21: ClassVar[PressableKeyboardKey]
    f22: ClassVar[PressableKeyboardKey]
    f23: ClassVar[PressableKeyboardKey]
    f24: ClassVar[PressableKeyboardKey]
    a: ClassVar[PressableKeyboardKey]
    b: ClassVar[PressableKeyboardKey]
    c: ClassVar[PressableKeyboardKey]
    d: ClassVar[PressableKeyboardKey]
    e: ClassVar[PressableKeyboardKey]
    f: ClassVar[PressableKeyboardKey]
    g: ClassVar[PressableKeyboardKey]
    h: ClassVar[PressableKeyboardKey]
    i: ClassVar[PressableKeyboardKey]
    j: ClassVar[PressableKeyboardKey]
    k: ClassVar[PressableKeyboardKey]
    l: ClassVar[PressableKeyboardKey]
    m: ClassVar[PressableKeyboardKey]
    n: ClassVar[PressableKeyboardKey]
    o: ClassVar[PressableKeyboardKey]
    p: ClassVar[PressableKeyboardKey]
    q: ClassVar[PressableKeyboardKey]
    r: ClassVar[PressableKeyboardKey]
    s: ClassVar[PressableKeyboardKey]
    t: ClassVar[PressableKeyboardKey]
    u: ClassVar[PressableKeyboardKey]
    v: ClassVar[PressableKeyboardKey]
    w: ClassVar[PressableKeyboardKey]
    x: ClassVar[PressableKeyboardKey]
    y: ClassVar[PressableKeyboardKey]
    z: ClassVar[PressableKeyboardKey]
    apostrophe: ClassVar[PressableKeyboardKey]
    backslash: ClassVar[PressableKeyboardKey]
    comma: ClassVar[PressableKeyboardKey]
    decimal_separator: ClassVar[PressableKeyboardKey]
    equals: ClassVar[PressableKeyboardKey]
    grave: ClassVar[PressableKeyboardKey]
    left_bracket: ClassVar[PressableKeyboardKey]
    minus: ClassVar[PressableKeyboardKey]
    non_us_backslash: ClassVar[PressableKeyboardKey]
    non_us_hash: ClassVar[PressableKeyboardKey]
    period: ClassVar[PressableKeyboardKey]
    right_bracket: ClassVar[PressableKeyboardKey]
    right_shift: ClassVar[PressableKeyboardKey]
    semicolon: ClassVar[PressableKeyboardKey]
    separator: ClassVar[PressableKeyboardKey]
    slash: ClassVar[PressableKeyboardKey]
    space: ClassVar[PressableKeyboardKey]
    tab: ClassVar[PressableKeyboardKey]
    thousands_separator: ClassVar[PressableKeyboardKey]
    again: ClassVar[PressableKeyboardKey]
    alt_erase: ClassVar[PressableKeyboardKey]
    start_application_1: ClassVar[PressableKeyboardKey]
    start_application_2: ClassVar[PressableKeyboardKey]
    context_menu: ClassVar[PressableKeyboardKey]
    backspace: ClassVar[PressableKeyboardKey]
    brightness_down: ClassVar[PressableKeyboardKey]
    brightness_up: ClassVar[PressableKeyboardKey]
    calculator: ClassVar[PressableKeyboardKey]
    cancel: ClassVar[PressableKeyboardKey]
    capslock: ClassVar[PressableKeyboardKey]
    clear: ClassVar[PressableKeyboardKey]
    clear_again: ClassVar[PressableKeyboardKey]
    computer: ClassVar[PressableKeyboardKey]
    copy: ClassVar[PressableKeyboardKey]
    crsel: ClassVar[PressableKeyboardKey]
    currency_sub_unit: ClassVar[PressableKeyboardKey]
    currency_unit: ClassVar[PressableKeyboardKey]
    cut: ClassVar[PressableKeyboardKey]
    delete: ClassVar[PressableKeyboardKey]
    display_switch: ClassVar[PressableKeyboardKey]
    eject: ClassVar[PressableKeyboardKey]
    end: ClassVar[PressableKeyboardKey]
    escape: ClassVar[PressableKeyboardKey]
    execute: ClassVar[PressableKeyboardKey]
    exsel: ClassVar[PressableKeyboardKey]
    find: ClassVar[PressableKeyboardKey]
    help: ClassVar[PressableKeyboardKey]
    home: ClassVar[PressableKeyboardKey]
    insert: ClassVar[PressableKeyboardKey]
    keyboard_illumination_down: ClassVar[PressableKeyboardKey]
    keyboard_illumination_toggle: ClassVar[PressableKeyboardKey]
    keyboard_illumination_up: ClassVar[PressableKeyboardKey]
    left_alt: ClassVar[PressableKeyboardKey]
    left_control: ClassVar[PressableKeyboardKey]
    left_special: ClassVar[PressableKeyboardKey]
    left_shift: ClassVar[PressableKeyboardKey]
    mail: ClassVar[PressableKeyboardKey]
    media_select: ClassVar[PressableKeyboardKey]
    menu: ClassVar[PressableKeyboardKey]
    mode: ClassVar[PressableKeyboardKey]
    mute: ClassVar[PressableKeyboardKey]
    numlock_clear: ClassVar[PressableKeyboardKey]
    oper: ClassVar[PressableKeyboardKey]
    out: ClassVar[PressableKeyboardKey]
    page_down: ClassVar[PressableKeyboardKey]
    page_up: ClassVar[PressableKeyboardKey]
    paste: ClassVar[PressableKeyboardKey]
    pause: ClassVar[PressableKeyboardKey]
    power: ClassVar[PressableKeyboardKey]
    print_screen: ClassVar[PressableKeyboardKey]
    prior: ClassVar[PressableKeyboardKey]
    right_alt: ClassVar[PressableKeyboardKey]
    right_control: ClassVar[PressableKeyboardKey]
    enter: ClassVar[PressableKeyboardKey]
    enter_2: ClassVar[PressableKeyboardKey]
    right_special: ClassVar[PressableKeyboardKey]
    scroll_lock: ClassVar[PressableKeyboardKey]
    select: ClassVar[PressableKeyboardKey]
    sleep: ClassVar[PressableKeyboardKey]
    stop: ClassVar[PressableKeyboardKey]
    system_request: ClassVar[PressableKeyboardKey]
    undo: ClassVar[PressableKeyboardKey]
    volume_down: ClassVar[PressableKeyboardKey]
    volume_up: ClassVar[PressableKeyboardKey]
    www: ClassVar[PressableKeyboardKey]
    audio_fast_forward: ClassVar[PressableKeyboardKey]
    audio_mute: ClassVar[PressableKeyboardKey]
    audio_next: ClassVar[PressableKeyboardKey]
    audio_play: ClassVar[PressableKeyboardKey]
    audio_previous: ClassVar[PressableKeyboardKey]
    audio_rewind: ClassVar[PressableKeyboardKey]
    audio_stop: ClassVar[PressableKeyboardKey]
    ac_back: ClassVar[PressableKeyboardKey]
    ac_bookmarks: ClassVar[PressableKeyboardKey]
    ac_forward: ClassVar[PressableKeyboardKey]
    ac_home: ClassVar[PressableKeyboardKey]
    ac_refresh: ClassVar[PressableKeyboardKey]
    ac_search: ClassVar[PressableKeyboardKey]
    ac_stop: ClassVar[PressableKeyboardKey]
    down: ClassVar[PressableKeyboardKey]
    left: ClassVar[PressableKeyboardKey]
    right: ClassVar[PressableKeyboardKey]
    up: ClassVar[PressableKeyboardKey]
    international_1: ClassVar[PressableKeyboardKey]
    international_2: ClassVar[PressableKeyboardKey]
    international_3: ClassVar[PressableKeyboardKey]
    international_4: ClassVar[PressableKeyboardKey]
    international_5: ClassVar[PressableKeyboardKey]
    international_6: ClassVar[PressableKeyboardKey]
    international_7: ClassVar[PressableKeyboardKey]
    international_8: ClassVar[PressableKeyboardKey]
    international_9: ClassVar[PressableKeyboardKey]
    numpad_0: ClassVar[PressableKeyboardKey]
    numpad_00: ClassVar[PressableKeyboardKey]
    numpad_000: ClassVar[PressableKeyboardKey]
    numpad_1: ClassVar[PressableKeyboardKey]
    numpad_2: ClassVar[PressableKeyboardKey]
    numpad_3: ClassVar[PressableKeyboardKey]
    numpad_4: ClassVar[PressableKeyboardKey]
    numpad_5: ClassVar[PressableKeyboardKey]
    numpad_6: ClassVar[PressableKeyboardKey]
    numpad_7: ClassVar[PressableKeyboardKey]
    numpad_8: ClassVar[PressableKeyboardKey]
    numpad_9: ClassVar[PressableKeyboardKey]
    numpad_a: ClassVar[PressableKeyboardKey]
    numpad_b: ClassVar[PressableKeyboardKey]
    numpad_c: ClassVar[PressableKeyboardKey]
    numpad_d: ClassVar[PressableKeyboardKey]
    numpad_e: ClassVar[PressableKeyboardKey]
    numpad_f: ClassVar[PressableKeyboardKey]
    numpad_ampersand: ClassVar[PressableKeyboardKey]
    numpad_at: ClassVar[PressableKeyboardKey]
    numpad_colon: ClassVar[PressableKeyboardKey]
    numpad_comma: ClassVar[PressableKeyboardKey]
    numpad_and: ClassVar[PressableKeyboardKey]
    numpad_or: ClassVar[PressableKeyboardKey]
    numpad_decimal: ClassVar[PressableKeyboardKey]
    numpad_divide: ClassVar[PressableKeyboardKey]
    numpad_enter: ClassVar[PressableKeyboardKey]
    numpad_equals: ClassVar[PressableKeyboardKey]
    numpad_as400_equals: ClassVar[PressableKeyboardKey]
    numpad_bang: ClassVar[PressableKeyboardKey]
    numpad_greater: ClassVar[PressableKeyboardKey]
    numpad_hash: ClassVar[PressableKeyboardKey]
    numpad_left_brace: ClassVar[PressableKeyboardKey]
    numpad_left_parenthesis: ClassVar[PressableKeyboardKey]
    numpad_less: ClassVar[PressableKeyboardKey]
    numpad_minus: ClassVar[PressableKeyboardKey]
    numpad_multiply: ClassVar[PressableKeyboardKey]
    numpad_percent: ClassVar[PressableKeyboardKey]
    numpad_period: ClassVar[PressableKeyboardKey]
    numpad_plus: ClassVar[PressableKeyboardKey]
    numpad_plus_minus: ClassVar[PressableKeyboardKey]
    numpad_power: ClassVar[PressableKeyboardKey]
    numpad_right_brace: ClassVar[PressableKeyboardKey]
    numpad_right_parenthesis: ClassVar[PressableKeyboardKey]
    numpad_space: ClassVar[PressableKeyboardKey]
    numpad_tab: ClassVar[PressableKeyboardKey]
    numpad_pipe: ClassVar[PressableKeyboardKey]
    numpad_xor: ClassVar[PressableKeyboardKey]
    numpad_backspace: ClassVar[PressableKeyboardKey]
    numpad_binary: ClassVar[PressableKeyboardKey]
    numpad_clear: ClassVar[PressableKeyboardKey]
    numpad_clear_entry: ClassVar[PressableKeyboardKey]
    numpad_hexadecimal: ClassVar[PressableKeyboardKey]
    numpad_octal: ClassVar[PressableKeyboardKey]
    numpad_memory_add: ClassVar[PressableKeyboardKey]
    numpad_memory_clear: ClassVar[PressableKeyboardKey]
    numpad_memory_divide: ClassVar[PressableKeyboardKey]
    numpad_memory_multiply: ClassVar[PressableKeyboardKey]
    numpad_memory_recall: ClassVar[PressableKeyboardKey]
    numpad_memory_store: ClassVar[PressableKeyboardKey]
    numpad_memory_subtract: ClassVar[PressableKeyboardKey]
    language_1: ClassVar[PressableKeyboardKey]
    language_2: ClassVar[PressableKeyboardKey]
    language_3: ClassVar[PressableKeyboardKey]
    language_4: ClassVar[PressableKeyboardKey]
    language_5: ClassVar[PressableKeyboardKey]
    language_6: ClassVar[PressableKeyboardKey]
    language_7: ClassVar[PressableKeyboardKey]
    language_8: ClassVar[PressableKeyboardKey]
    language_9: ClassVar[PressableKeyboardKey]

    def __init__(self, name: str, keyboard: Keyboard):
        super().__init__(name, keyboard=keyboard)
        self._is_pressed = False

    @property
    def is_pressed(self) -> bool:
        return self._is_pressed


class Keyboard(Peripheral):

    Event: type[KeyboardEvent]
    Connected: type[KeyboardConnected]
    Disconnected: type[KeyboardDisconnected]
    Focused: type[KeyboardFocused]
    LostFocus: type[KeyboardLostFocus]

    Key: type[PressableKeyboardKey]

    def __init__(self, name: str):
        super().__init__(name)
        class Event(KeyboardEvent, self.Event): # type: ignore
            pass
        self.Event = Event
        class Connected( # type: ignore
            KeyboardConnected,
            Event,
            self.Connected, # type: ignore
        ):
            pass
        self.Connected = Connected
        class Disconnected( # type: ignore
            KeyboardDisconnected,
            Event,
            self.Disconnected, # type: ignore
        ):
            pass
        self.Disconnected = Disconnected
        class Focused(KeyboardFocused, Event): # type: ignore
            pass
        self.Focused = Focused
        class LostFocus(KeyboardLostFocus, Event): # type: ignore
            pass
        self.LostFocus = LostFocus

        class Key(PressableKeyboardKey, keyboard=self):
            pass
        self.Key = Key

        self._window: Optional[Window] = None

    def __repr__(self) -> str:
        return f'<gamut.peripheral.Keyboard {self._name!r}>'

    @property
    def window(self) -> Optional[Window]:
        return self._window


def sdl_window_event_focus_gained(
    sdl_event: Any,
    mouse: Mouse,
    keyboard: Keyboard,
    controllers: dict[Any, Controller]
) -> Optional[KeyboardFocused]:
    try:
        window = get_window_from_sdl_id(sdl_event.window.windowID)
    except KeyError:
        return None
    assert keyboard._window is None
    keyboard._window = window
    return keyboard.Focused(window)

assert SDL_WINDOWEVENT_FOCUS_GAINED not in sdl_window_event_callback_map
sdl_window_event_callback_map[SDL_WINDOWEVENT_FOCUS_GAINED] = (
    sdl_window_event_focus_gained
)


def sdl_window_event_focus_lost(
    sdl_event: Any,
    mouse: Mouse,
    keyboard: Keyboard,
    controllers: dict[Any, Controller]
) -> KeyboardLostFocus:
    assert keyboard._window is not None
    keyboard._window = None
    return keyboard.LostFocus()

assert SDL_WINDOWEVENT_FOCUS_LOST not in sdl_window_event_callback_map
sdl_window_event_callback_map[SDL_WINDOWEVENT_FOCUS_LOST] = (
    sdl_window_event_focus_lost
)


def sdl_key_down_event_callback(
    sdl_event: Any,
    mouse: Mouse,
    keyboard: Keyboard,
    controllers: dict[Any, Controller]
) -> Optional[KeyboardKeyPressed]:
    if sdl_event.key.repeat != 0:
        return None
    sdl_scancode = sdl_event.key.keysym.scancode
    if sdl_scancode == SDL_SCANCODE_UNKNOWN:
        return None

    key: PressableKeyboardKey = getattr(
        keyboard.Key,
        sdl_scancode_to_gamut_key_name[sdl_scancode]
    )
    assert isinstance(key, PressableKeyboardKey)
    key._is_pressed = True
    return key.Pressed()

assert SDL_KEYDOWN not in sdl_event_callback_map
sdl_event_callback_map[SDL_KEYDOWN] = sdl_key_down_event_callback


def sdl_key_up_event_callback(
    sdl_event: Any,
    mouse: Mouse,
    keyboard: Keyboard,
    controllers: dict[Any, Controller]
) -> Optional[KeyboardKeyReleased]:
    assert sdl_event.key.repeat == 0
    sdl_scancode = sdl_event.key.keysym.scancode
    if sdl_scancode == SDL_SCANCODE_UNKNOWN:
        return None

    key: PressableKeyboardKey = getattr(
        keyboard.Key,
        sdl_scancode_to_gamut_key_name[sdl_scancode]
    )
    assert isinstance(key, PressableKeyboardKey)
    key._is_pressed = False
    return key.Released()

assert SDL_KEYUP not in sdl_event_callback_map
sdl_event_callback_map[SDL_KEYUP] = sdl_key_up_event_callback
