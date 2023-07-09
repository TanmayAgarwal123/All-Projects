import random
import pyautogui as pg
import time
def main():
    x=('aryan','hitesh','shravani','tanmay')
    #time.sleep(7)
    for i in range(2):
        a=random.choice(x)
        pg.write("@",a)
        pg.press("enter")
if __name__ == '__main__':
    main()    