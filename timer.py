import tkinter as tk
from datetime import datetime, timedelta

# 🔧 === CONFIGURATION VARIABLES === 🔧

# 🎯 Exam Date and Time
TARGET_YEAR = 2025
TARGET_MONTH = 5
TARGET_DAY = 1
TARGET_HOUR = 0
TARGET_MINUTE = 0
TARGET_SECOND = 0

# 💼 Job Timings (24-hr format)
JOB_START_HOUR = 9
JOB_START_MINUTE = 45
JOB_END_HOUR = 19
JOB_END_MINUTE = 15

# 🖼️ UI Style
WINDOW_POSITION_X = 200  
WINDOW_POSITION_Y = 0
PADDING_X = 5
PADDING_Y = 3
FONT_FAMILY = "Helvetica"
FONT_SIZE = 16
COLOR_BACKGROUND = "#001427"
COLOR_TEXT_MAIN = "#ecf0f1"
COLOR_TEXT_HIGHLIGHT = "#fb8500"

# 🕒 Target datetime object
target_time = datetime(
    TARGET_YEAR, TARGET_MONTH, TARGET_DAY, TARGET_HOUR, TARGET_MINUTE, TARGET_SECOND
)

# 🧠 === FUNCTIONS ===

def format_time(delta):
    total_seconds = int(delta.total_seconds())
    if total_seconds < 0:
        return "0 hrs 0 mins 0 secs"
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours} hrs {minutes} mins {seconds} secs"

def calculate_net_remaining_time(now, target):
    """Exclude job hours on Mon-Sat from net countdown"""
    total_net = timedelta()

    while now < target:
        if now.weekday() == 6:  # Sunday
            total_net += timedelta(minutes=1)
        else:
            job_start = now.replace(hour=JOB_START_HOUR, minute=JOB_START_MINUTE, second=0, microsecond=0)
            job_end = now.replace(hour=JOB_END_HOUR, minute=JOB_END_MINUTE, second=0, microsecond=0)

            if now < job_start or now >= job_end:
                total_net += timedelta(minutes=1)

        now += timedelta(minutes=1)

    return total_net

def update_timer():
    now = datetime.now()
    gross_remaining = target_time - now
    net_remaining = calculate_net_remaining_time(now, target_time)

    countdown_gross_label.config(text="Gross: " + format_time(gross_remaining))
    countdown_net_label.config(text="   Net: " + format_time(net_remaining) + " (Excludes job time)")

    root.after(1000, update_timer)

# 🪟 === MAIN WINDOW ===

root = tk.Tk()
root.configure(bg=COLOR_BACKGROUND)
root.overrideredirect(True)
root.attributes('-topmost', True)
root.geometry(f"+{WINDOW_POSITION_X}+{WINDOW_POSITION_Y}")

# 💠 Frame
frame = tk.Frame(root, bg=COLOR_BACKGROUND)
frame.pack(padx=PADDING_X, pady=PADDING_Y)

# 🕛 Labels on same line using one Frame
label_frame = tk.Frame(frame, bg=COLOR_BACKGROUND)
label_frame.pack(anchor="w")

countdown_gross_label = tk.Label(
    label_frame, font=(FONT_FAMILY, FONT_SIZE), fg=COLOR_TEXT_MAIN, bg=COLOR_BACKGROUND
)
countdown_gross_label.pack(side="left")

countdown_net_label = tk.Label(
    label_frame, font=(FONT_FAMILY, FONT_SIZE), fg=COLOR_TEXT_HIGHLIGHT, bg=COLOR_BACKGROUND
)
countdown_net_label.pack(side="left")

# 🔁 Start timer
update_timer()
root.mainloop()