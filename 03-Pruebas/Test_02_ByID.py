import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()

time.sleep(2)
nom=driver.find_element(by="id", value="userName")

nom.send_keys("Jose")
time.sleep(2)

driver.find_element(by="id", value="userEmail").send_keys("asd@gmail.com")
time.sleep(2)

driver.find_element(by="id",value="currentAddress").send_keys("descripcion")
time.sleep(2)

driver.find_element(by="id",value="permanentAddress").send_keys("direccion 2")
driver.execute_script("window.scrollTo(0, 500)")

time.sleep(2)
driver.find_element(by="id",value="submit").click()
time.sleep(5)

print(driver.title)
driver.close()