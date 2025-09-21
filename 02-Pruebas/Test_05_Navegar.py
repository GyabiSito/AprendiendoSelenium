import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
t=1

service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(t)
driver.get("https://www.selenium.dev/documentation/webdriver/elements/finders/")
time.sleep(t)
driver.get("https://github.com/nccgroup/VCG")
time.sleep(t)
driver.back() #Ojo, back frena cuando el tiempo de espera es largo
#Podemos reemplazarlo por:
driver.execute_script("window.history.go(-1)")
time.sleep(t)

driver.back()
time.sleep(t)
# driver.forward()
driver.execute_script("window.history.go(2)")

time.sleep(t)
driver.close()