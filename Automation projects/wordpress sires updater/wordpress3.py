from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def automate_site(browser, site, clicks, delay, replace_word_with="X"):
    browser.get(site)
    time.sleep(delay)

    for click in clicks:
        action = ActionChains(browser)
        action.move_by_offset(click[0], click[1]).click().perform()
        time.sleep(delay)

    # replace 'twitter' with 'X'
    body = browser.find_element_by_tag_name('body')
    body.send_keys(Keys.CONTROL + 'f')
    search_box = browser.switch_to.active_element
    search_box.send_keys('twitter')
    time.sleep(1)  # Let the search occur

    body.send_keys(Keys.CONTROL + 'h')
    time.sleep(1)  # Let the replace dialog appear

    # This part might change based on browser and its version
    # Assume you now have access to a 'find' input, a 'replace' input, and a 'replace all' button
    find_input = browser.switch_to.active_element
    find_input.send_keys('twitter')
    replace_input = browser.switch_to.active_element
    replace_input.send_keys(replace_word_with)

    replace_all_button = browser.find_element_by_id('replace-all-button-id')  # Modify this to the correct selector
    replace_all_button.click()
    time.sleep(delay)

    # Second click
    action = ActionChains(browser)
    action.move_by_offset(clicks[1][0], clicks[1][1]).click().perform()
    time.sleep(delay)

sites = ['http://www.example.com', 'http://www.example2.com']
clicks = [(100, 200), (300, 400)]  # [(x1, y1), (x2, y2)]
delay = 5  # seconds

with webdriver.Chrome(executable_path='path_to_chromedriver.exe') as browser:
    for site in sites:
        automate_site(browser, site, clicks, delay)
