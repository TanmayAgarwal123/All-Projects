import pyautogui as pg
import time

messages = ['Hii', 'Hii 2','Hii 3', '']

# Wait for some time before starting the messages
time.sleep(5)

for message in messages:
    pg.write(message)
    pg.press("enter")
    time.sleep(60)
