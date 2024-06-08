# 🔑 Keylogger Project 🔑
---
## Overview 🔒
*The **Keylogger project** is a Python-based application designed to capture and log keystrokes in real-time. It offers a range of features including email notifications, periodic data reporting, error logging, and more. This project demonstrates the use of Python for creating a powerful monitoring tool, while adhering to ethical guidelines and security practices.*

## Features 👇👇👇
- Real-time Keystroke Logging: Captures all keystrokes in real-time.
- Start/Stop Commands: Controlled via 'Ctrl+Alt+s' to start and 'Ctrl+Alt+x' to stop.
- Email Notifications: Sends daily logs to a specified email address at 9:00 PM.
- Periodic Reporting: Outputs log every 100 keystrokes and prompts the user to save the log.
- Error Logging: Records any errors or exceptions to an error log file.
- Auto Save on Exit: Automatically saves the log when the program exits.

## Technologies Used 💽
- **Programming Language:**  Python
- **Libraries:** pynput, smtplib, schedule, threading, atexit
- **Email Service:** SMTP (Gmail)

## Installation  🎁🎁🎁
---
1. **Clone the repository:**
``` sh
git clone https://github.com/yourusername/keylogger.git
cd keylogger
```
2. **Create a virtual environment (optional but recommended):**
``` sh 
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. **Install the required libraries:**
``` sh 
pip install pynput schedule
```
4. **Update email credentials:** <br>
- Open the keylogger.py file.
- Replace "your_email@gmail.com" and "your_email_password" with your actual email credentials.

## Usage
1. **Run the keylogger:**
``` sh
python keylogger.py
```
2. **Control the keylogger:**

- Press Ctrl+Alt+s to start logging.
- Press Ctrl+Alt+x to stop logging.

## Key Functions:  🔐🔐 <br>
- **grab_keys(key):** Captures and processes each keystroke.
- **ask_to_save():** Prompts the user to save the log every 100 keystrokes.
- **report():** Periodically outputs the log.
- **send_email(log_content):** Sends the log content via email.
- **daily_email():** Schedules the daily email task.
- **save_on_exit():** Saves the log on program exit.

## Ethical Considerations 👨🏻‍💻 👁️
*This project is intended for educational purposes only. Ensure you have explicit permission to use this keylogger on any device. Unauthorized use of keyloggers can be illegal and unethical.*
## License 🕵️‍♂️
*This project is licensed under the MIT License. See the <LICENSE> file for details.*