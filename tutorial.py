from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()
driver.get("https://www.twitch.tv/directory/category/art")

# configure webdriver
options = Options()

# Hides GUI
options.headless = True

# Set window size to native GUI size
options.add_argument("--window-size=1920,1080")

# ensure window is full-screen
options.add_argument("start-maximized")
