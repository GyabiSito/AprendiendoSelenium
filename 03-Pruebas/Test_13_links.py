import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

t = 1

service = Service(r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("file:///C:/Users/Josec/OneDrive/Escritorio/Selenium/03-Pruebas/links.html")
driver.maximize_window()
time.sleep(t)
# Obteniendo todos los links de la pàgina
links = driver.find_elements(By.TAG_NAME, "a")
print("El numero de Links que hay en la pàgina es: ", len(links))
for num in links: print(num.text)
driver.find_element(By.LINK_TEXT, "Date pickers").click()
time.sleep(t)
driver.find_element(By.LINK_TEXT, "JQuery Date Picker").click()
time.sleep(t)
time.sleep(t)
driver.close()
