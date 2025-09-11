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

driver.get("https://pixabay.com/es/")
driver.maximize_window()
time.sleep(t)

#driver.execute_script("window.scrollTo(0,1500)")


try:
    Buscar = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/es/images/search/?order=ec'][contains(.,'Descubre más')]")))
    Buscar=driver.find_element("xpath","//a[@href='/es/images/search/?order=ec'][contains(.,'Descubre más')]")
    ir=driver.execute_script("arguments[0].scrollIntoView();",Buscar)
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")





time.sleep(t)
driver.close()