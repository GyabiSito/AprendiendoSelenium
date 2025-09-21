import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
t=1

service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
driver.implicitly_wait(15) #Tienes hasta 15 segundos hasta que tire error si no encuentra el elemento
time.sleep(t)

nom=driver.find_element(by="xpath", value="//input[contains(@id,'userName')]")

nom.send_keys("Jose")
driver.find_element(by="xpath", value="//input[contains(@id,'userEmail')]").send_keys("asd@gmail.com")
driver.find_element(by="xpath",value="//textarea[contains(@id,'currentAddress')]").send_keys("descripcion")
driver.find_element(by="xpath",value="//textarea[contains(@id,'permanentAddress')]").send_keys("direccion 2")

driver.execute_script("window.scrollTo(0, 500)")
driver.find_element(by="xpath",value="//button[contains(@id,'submit')]").click()

time.sleep(t)
driver.close()