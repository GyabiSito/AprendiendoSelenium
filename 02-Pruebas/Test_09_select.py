import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

t = 1

service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("file:///C:/Users/Josec/OneDrive/Escritorio/Selenium/02-Pruebas/select.html")
driver.maximize_window()
select1 = driver.find_element(by="xpath", value="//select[contains(@id,'select-demo')]")
dias = Select(select1)
dias.select_by_visible_text("Sunday")
time.sleep(t)
dias.select_by_index(2)
time.sleep(t)
dias.select_by_value("Thursday")
time.sleep(t)
# segundo bloque ciudad=Select(driver.find_element_by_id("multi-select")) ciudad.select_by_value("California") time.sleep(t) ciudad.select_by_value("New York") time.sleep(t) ciudad.select_by_index(2) time.sleep(t) driver.close()

driver.close()
