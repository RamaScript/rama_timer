import tkinter as tk
from datetime import datetime

# 🔧 === CONFIGURATION VARIABLES (Easy to Edit) === 🔧

# 🎯 Target Date and Time {24hrs}
TARGET_YEAR = 2025
TARGET_MONTH = 5
TARGET_DAY = 1
TARGET_HOUR = 0
TARGET_MINUTE = 0
TARGET_SECOND = 0

# 🎨 Colors
COLOR_BACKGROUND = "#001427"
COLOR_TEXT_MAIN = "#ecf0f1"
COLOR_TEXT_HIGHLIGHT = "#fb8500"

# 📐 Layout
WINDOW_POSITION_X = 600
WINDOW_POSITION_Y = 0
PADDING_X = 5
PADDING_Y = 3

# 🆎 Font
FONT_FAMILY = "Helvetica"
FONT_SIZE = 20

# 🕒 Target time from variables
target_time = datetime(
    TARGET_YEAR, TARGET_MONTH, TARGET_DAY, TARGET_HOUR, TARGET_MINUTE, TARGET_SECOND
)

# 🧠 === FUNCTIONS ===

def format_time(delta):
    """Convert timedelta to hours, minutes, seconds format"""
    total_seconds = int(delta.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours} hours {minutes} mins {seconds} secs"

def update_timer():
    now = datetime.now()
    remaining_time = target_time - now
    if remaining_time.total_seconds() > 0:
        countdown_text = format_time(remaining_time)
        countdown_label.config(
            text=countdown_text,
            bg=COLOR_BACKGROUND,
            fg=COLOR_TEXT_HIGHLIGHT
        )
    else:
        countdown_label.config(
            text="The countdown has ended!",
            bg=COLOR_BACKGROUND,
            fg=COLOR_TEXT_HIGHLIGHT
        )
    root.after(1000, update_timer)

# 🪟 === MAIN WINDOW ===

root = tk.Tk()
root.configure(bg=COLOR_BACKGROUND)
root.overrideredirect(True)       # ❌ Remove title bar
root.attributes('-topmost', True) # 📌 Always on top
root.geometry(f"+{WINDOW_POSITION_X}+{WINDOW_POSITION_Y}")

# 💠 Frame
frame = tk.Frame(root, bg=COLOR_BACKGROUND)
frame.pack(padx=PADDING_X, pady=PADDING_Y)

# ⏳ Countdown Label
countdown_label = tk.Label(
    frame,
    font=(FONT_FAMILY, FONT_SIZE),
    anchor="w",
    bg=COLOR_BACKGROUND,
    fg=COLOR_TEXT_HIGHLIGHT
)
countdown_label.pack(side="left", padx=PADDING_X)

# 🔁 Start the timer loop
update_timer()
root.mainloop()
