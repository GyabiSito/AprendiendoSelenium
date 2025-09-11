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
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox")
driver.maximize_window()
driver.find_element(By.XPATH, "//button[contains(@id,'runbtn')]").click()
driver.find_element(By.ID, "vehicle1").click()

time.sleep(t)
btn3=driver.find_element(By.ID, "vehicle3")
btn3.click()
time.sleep(t)
sub=driver.find_element(By.XPATH, "//input[@type='submit']")
sub.click()
time.sleep(t)





driver.close()


