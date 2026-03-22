import board
import microcontroller
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC, make_key
from kmk.scanners import DiodeOrientation
from kmk.handlers.sequences import send_string

# ─────────────────────────────────────────────
# HARDWARE CONFIGG
# ─────────────────────────────────────────────

COLS = (board.D0, board.D1, board.D2)
ROWS = (board.D8, board.D9, board.D10)
DIODE_ORIENTATION = DiodeOrientation.COL2ROW

# ─────────────────────────────────────────────
# CONFIGG
# ─────────────────────────────────────────────

HABITS = [
    {"name": "SAT",    "url": "https://www.oneprep.xyz/\n"},  
    {"name": "Read",    "url": None},                          
    {"name": "Sleep", "url": None},                          
    {"name": "Water",     "url": None},                          
    {"name": "Good",  "url": None},                         
]

# ─────────────────────────────────────────────
# TIMER CONFIG (minutes)
# ─────────────────────────────────────────────

TIMER_DURATIONS = [10, 30]

# ─────────────────────────────────────────────
# STATE
# ─────────────────────────────────────────────

habit_state = bytearray([0])

def _load_state():
    if len(microcontroller.nvm) > 0:
        habit_state[0] = microcontroller.nvm[0]

def _save_state():
    if len(microcontroller.nvm) > 0:
        microcontroller.nvm[0] = habit_state[0]

def _reset_state():
    habit_state[0] = 0
    _save_state()

# ─────────────────────────────────────────────
# Handle Keys
# ─────────────────────────────────────────────

def toggle_habit(key, keyboard, *args, **kwargs):
    idx = key.meta.habit_idx
    habit = HABITS[idx]

    habit_state[0] ^= (1 << idx)
    _save_state()

    if habit["url"]:
        send_string(habit["url"])

    is_active = bool(habit_state[0] & (1 << idx))
    print(f"[HABIT] '{habit['name']}' {'ON' if is_active else 'OFF'} | state={bin(habit_state[0])}")


def start_timer(key, keyboard, *args, **kwargs):
    minutes = key.meta.minutes
    print(f"[TIMER] Starting {minutes}-minute timer")
    # TODO Timer logic implmentation


def sync_and_reset(key, keyboard, *args, **kwargs):
    send_string(f"{bin(habit_state[0])}\n")
    _reset_state()
    print("[SYNC] State exported and reset")

# ─────────────────────────────────────────────
# Define keys
# ─────────────────────────────────────────────

habit_keys = [
    make_key(on_press=toggle_habit, meta={"habit_idx": i})
    for i in range(len(HABITS))
]

timer_keys = [
    make_key(on_press=start_timer, meta={"minutes": m})
    for m in TIMER_DURATIONS
]

SYNC = make_key(on_press=sync_and_reset)

H1, H2, H3, H4, H5 = habit_keys
T10, T30 = timer_keys

# ─────────────────────────────────────────────
# Keyboard SETUP
# ─────────────────────────────────────────────

keyboard = KMKKeyboard()

keyboard.col_pins = COLS
keyboard.row_pins = ROWS
keyboard.diode_orientation = DIODE_ORIENTATION

keyboard.keymap = [
    [
        H1,  H2,  H3,
        H4,  H5,  T10,
        T30, SYNC, KC.NO,  # KC.NO = empty/unused key
    ]
]

# ─────────────────────────────────────────────
# Main Loop
# ─────────────────────────────────────────────

if __name__ == "__main__":
    _load_state()
    print(f"[BOOT] Habit state loaded: {bin(habit_state[0])}")
    keyboard.go()