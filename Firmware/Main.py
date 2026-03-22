import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D0, board.D1, board.D2) 
keyboard.row_pins = (board.D8, board.D9, board.D10)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.A,    KC.B,    KC.C,
        KC.D,    KC.E,    KC.F,
        KC.G,    KC.H,    KC.I,
    ]
]

if __name__ == '__main__':
    keyboard.go()