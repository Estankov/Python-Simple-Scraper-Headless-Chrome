from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36")
options.add_argument("--window-size=1920,1080")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.maximize_window()

url = 'https://investor.vanguard.com/investment-products/mutual-funds/profile/vfiax'
    
browser.get(url)

time.sleep(5)

nav = browser.find_element('xpath', '/html/body/vmf-root/profile/div/dashboard/section/div[2]/div/div[2]/dashboard-stats/div/div[4]/div[2]')
print(nav.text)
print('----')
ytd = browser.find_element('xpath', '/html/body/vmf-root/profile/div/div[2]/overview/section/div/div/div[2]/div/div[1]/performance/div/div[2]')
print(ytd.text)

browser.quit()




