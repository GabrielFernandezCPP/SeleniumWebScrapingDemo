from parsel import Selector

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# configure webdriver #
options = Options()

# Hides GUI
options.headless = True

# Set window size to native GUI size
options.add_argument("--window-size=1920,1080")

# ensure window is full-screen
options.add_argument("start-maximized")

# Dont load images or javascript #
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(
    #Disables image loading
    "prefs", {"profile.managed_default_content_settings.images": 2}
)

#NOTE THE CURRENT TUTORIAL IS OUT OF DATE. SELENIUM WAS UPDATED
#TO REMOVE A BUNCH OF THINGS FROM THE INIT CLASS OF webdriver. chrome_options WAS ONE OF THEM.
#WORK AROUND.

driver = webdriver.Chrome(options=chrome_options)#, chrome_options=chrome_options)
driver.get("https://www.twitch.tv/directory/category/art")

# wait for page to load
element = WebDriverWait(driver=driver, timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-target=directory-first-item]')))
#driver.quit()

print(driver.page_source)

sel = Selector(text=driver.page_source)
parsed = []

for item in sel.xpath("//div[contains(@class,'tw-tower')]/div[@data-target]"):
    parsed.append({
        'title': item.css('h3::text').get(),
        'url': item.css('.tw-link::attr(href)').get(),
        'username': item.css('.tw-link::text').get(),
        'tags': item.css('.tw-tag ::text').getall(),
        'viewers': ''.join(item.css('.tw-media-card-stat::text').re(r'(\d+)')),
    })

print('\n')
print(parsed)