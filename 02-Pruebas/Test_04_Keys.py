import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()

time.sleep(2)
nom=driver.find_element(By.CSS_SELECTOR, value="#userName")
nom.send_keys("Jose")
time.sleep(2)
nom.send_keys(Keys.TAB + "jose@gmail.com" + Keys.TAB + "Direccion 1" + Keys.TAB + "Direccion 2" + Keys.TAB + Keys.ENTER)

driver.execute_script("window.scrollTo(0, 500)")

time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,value="#submit").click()
# driver.find_element(by="css selector",value="#submit").click()
time.sleep(5)

driver.find_element(by=By.XPATH, value="//li[@class='btn btn-light '][contains(.,'Check Box')]").click()
time.sleep(2)

print(driver.title)
driver.close()