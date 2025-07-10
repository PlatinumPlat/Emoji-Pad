import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.TX, board.RX, board.SCK, board.MISO, board.MOSI]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

macros.macros = [
    Tap(['👍']),   # MACRO_0
    Tap(['🤣']),   # MACRO_1
    Tap(['💀']),   # MACRO_2
    Tap(['🔥']),   # MACRO_3
    Tap(['😃']),   # MACRO_4
]

keyboard.keymap = [
    [KC.MACRO_0, KC.MACRO_1, KC.MACRO_2, KC.MACRO_3, KC.MACRO_4]
]

if __name__ == '__main__':
    keyboard.go()