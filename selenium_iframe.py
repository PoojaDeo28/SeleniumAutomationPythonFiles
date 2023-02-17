from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from selenium.webdriver.support.select import Select

service_object=Service("C:\Chrome Driver\chromedriver_win32\chromedriver.exe")
# set chrome driver.exe path
driver=webdriver.Chrome(service=service_object)
driver.implicitly_wait(5)
#print(dir(webdriver))
#url lunch
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

#link_text
#driver.find_element(By.LINK_TEXT,"org.openqa.selenium.devtools.idealized.log").click()--wrong approach

#switch into frame
#switch_to.frame(name)
#switch_to.frmae(id)
driver.switch_to.frame("packageListFrame")#first frame
#time.sleep(3)
driver.find_element(By.LINK_TEXT,"org.openqa.selenium.devtools").click()
time.sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame("packageFrame")#frame 2
driver.find_element(By.LINK_TEXT,"Connection").click()
time.sleep(2)
driver.switch_to.default_content()


driver.switch_to.frame("classFrame")# frame 3

driver.find_element(By.XPATH,"//html/body/header/nav/div[1]/div[1]/ul/li[6]").click()
time.sleep(2)
driver.switch_to.default_content()



time.sleep(3)
driver.close()