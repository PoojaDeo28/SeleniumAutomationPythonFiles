from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service_object=Service("C:\Chrome Driver\chromedriver_win32\chromedriver.exe")
# set chrome driver.exe path
driver=webdriver.Chrome(service=service_object)
#print(dir(webdriver))


#url lunch
driver.get('https://rahulshettyacademy.com/client')
time.sleep(5.0)
#driver.find_element(By.LINK_TEXT,"Forgot password?").click()

driver.find_element(By.PARTIAL_LINK_TEXT,"Forgot").click()
time.sleep(10)
driver.close()