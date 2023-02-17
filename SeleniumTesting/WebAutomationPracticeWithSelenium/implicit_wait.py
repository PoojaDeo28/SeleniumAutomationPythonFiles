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
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(3)
ber_products= driver.find_elements(By.XPATH,"//div[@class='products']/div")
count=len(ber_products)

#print(count)
assert count>0

#selenium chaining
for button_products in ber_products:
    button_products.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[@type='button']").click()
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

# sum validation
product_price=driver.find_elements(By.XPATH,"//tr/td[5]/p")
#print(len(product_price))
sum=0

for price in product_price:
    sum=sum+int(price.text)
print('checking: ',sum)
total_amount=driver.find_element(By.CSS_SELECTOR,".totAmt").text
print('output',total_amount)

assert sum==int(total_amount)


#Explicit wait

wait = WebDriverWait(driver,10)
#print(dir(wait))
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
msg=driver.find_element(By.CSS_SELECTOR,".promoInfo").text
print(msg)
#print(msg)
#assert "Code applied ..!"== msg
time.sleep(8)
driver.close()
