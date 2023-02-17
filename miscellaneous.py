from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

service_object=Service("C:\Chrome Driver\chromedriver_win32\chromedriver.exe")
# set chrome driver.exe path
driver=webdriver.Chrome(service=service_object)

#print(dir(webdriver))


#url lunch
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)
driver.execute_script("window.scrollBy(0,500)")
driver.get_screenshot_as_file("screenshot_1.png")
time.sleep(5)
driver.close()