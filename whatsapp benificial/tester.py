import webbrowser
import pyautogui as pg
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
url = "https://web.whatsapp.com/send?phone=9982219151&text=hello&app_absent=1"
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open(url)
time.sleep(10)

browser = webdriver.Chrome(r"C:/Program Files/Google/Chrome/Application/chrome.exe")
time.sleep(5)
enter_action = ActionChains(browser)
enter_action.send_keys(Keys.ENTER)
pg.press("enter")
