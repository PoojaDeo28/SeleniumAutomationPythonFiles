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
driver.get("https://rahulshettyacademy.com/angularpractice/")

#There are 8 locators in selenium
#ID, NAME,CLASSNAME,TAGNAME,LINKTEXT,PARTIAL LINK TEXT,CSS_SELECTORS,XPATH

#driver.find_element(By.NAME, "name").send_keys("kalyan")
#CSS_SELECTOR
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys('Scodeen')
driver.find_element(By.NAME, "email").send_keys("kalyan@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("xyzall")
driver.find_element(By.ID, "exampleFormControlSelect1").send_keys("Male")
#driver.find_element(By.CLASS_NAME, "btn-success").click()

#XPATH

#XPATH: RELATIVE XPATH AND ABSOLUTE XPATH

#RELATIVE XPATH: //tagname[@attribute='value']
#note: if relativexpath showing multiple results then we can use [1],[2],... for selecting
#1st, 2nd, ...element like (By.XPATH,"//input[@type='submit'][1]").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()

#static dropdown
static_drop_down = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
#static_drop_down.select_by_visible_text("Female") #using text
#static_drop_down.select_by_index(1)  #using index shows female because pythn index starts with 0
static_drop_down.select_by_index(0)

#ABSOLUTE XPATH for radio button(nothing but CSS_SELECTOR)
#driver.find_element(By.XPATH,"//form/div[6]/div[1]/input").click()

#CSS_SELECTOR for radio button(in css_selector, div counting starts from 2 but in Relative XPATH, div counting starts from 1)
#driver.find_element(By.CSS_SELECTOR,'form div:nth-child(7) div input').click()
# if we want 2nd radio button
#driver.find_element(By.CSS_SELECTOR,'form div:nth-child(7) div:nth-child(3) input').click()

#LINK TEXT and PARTIAL LINK TEXT

#This line showing error. driver.find_element(By.PARTIAL_LINK_TEXT,"Student").click()

#CSS_SELECTORS:- tagname[attribute='value']

message=driver.find_element(By.CLASS_NAME, "alert-dismissible").text
print(message)
assert 'Success!' in message
time.sleep(5.00)



driver.close()

#There are 8 locators in selenium
#ID, NAME,CLASSNAME,TAGNAME,LINKTEXT,PARTIAL LINK TEXTCSS_SELECTORS,XPATH
