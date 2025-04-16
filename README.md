# 📅 Exam Countdown Timer with Gross & Net Time Tracking

A minimal desktop application built using **Python and Tkinter** to help you track time remaining until your exams. This app not only shows the **gross time** left until the exam but also calculates the **net productive time** available by excluding:

- 💤 Daily sleep hours (customizable)
- 💼 Job/work hours (only on weekdays)

---

## 🛠️ Features

- 📆 Countdown to a specific exam date and time.
- 🕐 Shows both **Gross** and **Net** time remaining.
- ⏰ Excludes:
  - Sleep time (every day, customizable start and end).
  - Job time (Monday to Saturday).
- ⚡ Lightweight and always-on-top window.
- 🎨 Customizable UI and time parameters.

---

## 🧪 Example

If your exam is on **May 1, 2025**, and you:
- Sleep from **11:00 PM to 6:00 AM**
- Work from **9:45 AM to 7:15 PM**, Monday to Saturday

The timer will:
- Show total (gross) time left until the exam.
- Subtract your sleep + job hours from it and show productive (net) time remaining.

---

## 🧑‍💻 Requirements

- Python 3.x
- Tkinter (usually pre-installed with Python)

---

## 🧾 How to Use

1. Clone or download this repository.

2. Open the Python file in your favorite editor (e.g., VS Code, PyCharm).

3. Customize the following variables as per your schedule:
   ```python
   TARGET_YEAR = 2025
   TARGET_MONTH = 5
   TARGET_DAY = 1
   TARGET_HOUR = 0
   TARGET_MINUTE = 0
   TARGET_SECOND = 0

   JOB_START_HOUR = 9
   JOB_START_MINUTE = 45
   JOB_END_HOUR = 19
   JOB_END_MINUTE = 15

   SLEEP_START_HOUR = 23  # 11 PM
   SLEEP_END_HOUR = 6     # 6 AM
