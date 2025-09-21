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

driver.get("https://testpages.herokuapp.com/styled/file-upload-test.html")
driver.maximize_window()
time.sleep(t)

try:
    Buscar = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'fileinput')]")))
    Buscar = driver.find_element("xpath","//input[contains(@id,'fileinput')]")
    Buscar.send_keys("C:\\Users\\Josec\\OneDrive\\Escritorio\\Gh6Z6DUWQAEZZQu.jpg")
    time.sleep(t)
    driver.find_element("xpath","//input[contains(@id,'itsanimage')]").click()
    driver.find_element("xpath","//input[contains(@type,'submit')]").click()
    time.sleep(t)



except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")

time.sleep(t)
driver.close()
