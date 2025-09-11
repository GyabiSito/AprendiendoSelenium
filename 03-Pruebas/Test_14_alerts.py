import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

service = Service(r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
t = 2


driver.get("file:///C:/Users/Josec/OneDrive/Escritorio/Selenium/03-Pruebas/alerts.html")
driver.maximize_window()
time.sleep(t)


driver.find_element(By.XPATH, "//a[@href='#myModal0']").click()
time.sleep(t)

# Esperar a que el botón "Save changes" sea clickeable
try:
    boton_save = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "(//a[@href='#'][contains(.,'Save changes')])[1]"))
    )
    boton_save.click()
    print("Botón 'Save changes' clickeado con éxito.")
    time.sleep(t)

except TimeoutException as ex:
    print("Error: El botón no estuvo disponible a tiempo.", ex.msg)

time.sleep(3)
driver.close()
