from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
# Replace below path with the absolute path
browser = webdriver.Chrome(r"C:/Program Files/Google/Chrome/Application/chrome.exe")
phone = "9982219151"
message = "hello"
url = "https://web.whatsapp.com/send?phone="+ phone + "&text=" + message + "&app_absent=1"
# Load Whatsapp Web page
browser.get(url)
# Wait for the page be loaded
time.sleep(5)
enter_action = ActionChains(browser)
enter_action.send_keys(Keys.ENTER)
# Send message
enter_action.perform()
# Close browser
browser.close()