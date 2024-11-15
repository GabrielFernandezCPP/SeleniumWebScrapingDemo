from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#NOTE HAD TO CHANGE THE find_element_by_css_selector AS IT WAS REMOVED AND REPLACED

driver = webdriver.Chrome()
driver.get("https://www.twitch.tv/")
search_box = driver.find_element(By.CSS_SELECTOR,'input[aria-label="Search Input"]') 
search_box.send_keys(
    'fast painting'
)
# either press the enter key
search_box.send_keys(Keys.ENTER)
# or click search button
search_button = driver.find_element(By.CSS_SELECTOR, 'button[icon="NavSearch"]')
search_button.click()