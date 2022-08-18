from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time
import os, time

driver = webdriver.Chrome(service=Service("C:/Users/User/Desktop/Selenium/chromedriver.exe"))

driver.get("https://web.whatsapp.com/")
time.sleep(10)

celular = "542234472465"
mensaje = "Hola, desde el BOT Python :B"

driver.get("https://wa.me/"+celular+"?text="+mensaje)
time.sleep(5)

btn = driver.find_element(By.XPATH, "//*[@id='action-button']")
btn.click()
time.sleep(5)

btn = driver.find_element(By.XPATH, "//*[@id='fallback_block']/div/div/h4[2]/a")
btn.click()
time.sleep(10)

btn = driver.find_element(By.CSS_SELECTOR, 'a.button.button--simple.button--primary')
btn.click()
time.sleep(5)

print("-- End of BOT --")

driver.close()