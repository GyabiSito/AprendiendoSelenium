import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

t = 1

service = Service(r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox")
driver.maximize_window()

# Cambiamos al iframe que contiene el formulario
driver.switch_to.frame("iframeResult")


chk1 = driver.find_element(By.ID, "vehicle1")
chk1.click()
time.sleep(t)

chk3 = driver.find_element(By.ID, "vehicle3")
chk3.click()
time.sleep(t)


sub = driver.find_element(By.XPATH, "//input[@type='submit']")
sub.click()
time.sleep(t)

driver.close()
