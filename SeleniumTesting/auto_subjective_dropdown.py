from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

service_object=Service("C:\Chrome Driver\chromedriver_win32\chromedriver.exe")
# set chrome driver.exe path
driver=webdriver.Chrome(service=service_object)
#print(dir(webdriver))


#url lunch
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

#Dynamic dropdown
driver.find_element(By.ID,"autosuggest").send_keys("Ind")
time.sleep(3)
#driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
#here 'ind' will return 3 countries, it means find.elements returns output in list.
countries=driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")

print(len(countries))
for country in countries:
    print(country.text)
time.sleep(5)
driver.close()
