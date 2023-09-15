from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuration
CHROME_DRIVER_PATH = 'C:/webdriver/chromedriver'
SITES = [
    {
        'url': 'https://site1.com/wp-login.php',
        'username': 'tanmay',
        'password': 'j17EAzP9uW6g5EAmUZnR0Y!2'
    },
    # Add more sites as needed
]

def login_and_replace(driver, site_info):
    driver.get(site_info['url'])
    
    # Login to WordPress
    driver.find_element(By.ID, 'tanmay').send_keys(site_info['username'])
    driver.find_element(By.ID, 'j17EAzP9uW6g5EAmUZnR0Y!2').send_keys(site_info['password'])
    driver.find_element(By.ID, 'wp-submit').click()
    
    # Wait and navigate to Posts after logging in
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'menu-posts')))
    driver.find_element(By.ID, 'menu-posts').click()

    # Assuming 'All Posts' opens up by default, we'll start editing the posts.
    # Adjust this as needed based on your WordPress setup.
    # Note: This will work for a few posts; you might need to handle pagination for many posts.
    
    post_links = driver.find_elements(By.XPATH, "//td[@data-colname='Title']//a[contains(text(), 'Edit')]")
    for link in post_links:
        link.click()  # Click to edit post

        # Find the content editor and replace content
        content_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'content')))
        content = content_box.get_attribute('value')  # Get current content
        updated_content = content.replace('twitter', 'xtwitter')  # Replace word
        content_box.clear()  # Clear existing content
        content_box.send_keys(updated_content)  # Input updated content
        
        # Update the post
        driver.find_element(By.ID, 'publish').click()
        time.sleep(3)  # Wait a bit before editing the next post

    # Log out (optional)
    driver.get(site_info['url'].replace('wp-login.php', 'wp-login.php?action=logout'))
    driver.find_element(By.LINK_TEXT, 'log out').click()

# Set up Selenium driver
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

for site in SITES:
    login_and_replace(driver, site)

driver.quit()
