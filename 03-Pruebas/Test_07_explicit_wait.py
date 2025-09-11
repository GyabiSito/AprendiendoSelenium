import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

t=1

service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("file:///C:/Users/Josec/OneDrive/Escritorio/Selenium/03-Pruebas/modal.html")
driver.maximize_window()
driver.implicitly_wait(15)
#Explicit wait, vamos a esperar un elemento y, cuando salga, vamos a accionar ciertas cosas
modal = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "myModal")))
close_btn = modal.find_element(By.CSS_SELECTOR, "button.close")
close_btn.click()

time.sleep(t)

driver.find_element(By.ID, "nombre").send_keys("Juan Pérez")
driver.find_element(By.ID, "email").send_keys("juan@example.com")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(3)




driver.close()