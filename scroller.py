from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

s = Service('usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://www.tiktok.com/')

body = driver.find_element(by=By.TAG_NAME, value='body')

while True:
    body.send_keys(Keys.DOWN)
    time.sleep(0.5)
