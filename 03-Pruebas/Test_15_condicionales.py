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


driver.get("https://demoqa.com/")
driver.maximize_window()

titulo=driver.find_element(By.XPATH,"//img[@src='/images/Toolsqa.jpg']")
print(titulo.is_displayed())
btn1=driver.find_element(By.XPATH,"(//div[contains(@class,'card-up')])[1]")

if(titulo.is_displayed()==True):
    print("Existe la imagen")
    btn1.click()
    time.sleep(2)
else:
    print("No existe la imagen")


time.sleep(2)
driver.close()