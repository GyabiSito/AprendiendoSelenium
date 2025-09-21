import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

t = 1

try:
    service = Service(r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("file:///C:/Users/Josec/OneDrive/Escritorio/Selenium/02-Pruebas/select.html")
    driver.maximize_window()

    select1 = driver.find_element(By.XPATH, "//select[contains(@id,'select-demo')]")
    dias = Select(select1)
    dias.select_by_visible_text("Sunday")
    time.sleep(t)

    dias.select_by_index(2)
    time.sleep(t)

    dias.select_by_value("Thursday")
    time.sleep(t)

    ciudad = Select(driver.find_element(By.ID, "multi-select"))
    ciudad.select_by_value("California")
    time.sleep(t)
    ciudad.select_by_value("New York")
    time.sleep(t)
    ciudad.select_by_index(2)
    time.sleep(t)

except Exception as e:
    print(f" Error durante la ejecución: {e}")

finally:
    driver.quit()
