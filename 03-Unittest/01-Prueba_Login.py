import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
t = 2


class PruebaLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def test_login1(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        nom = driver.find_element(By.XPATH, "//input[@id='user-name']")
        password = driver.find_element(By.XPATH, "//input[@id='password']")
        boton = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("admin")
        password.send_keys("admin123")
        boton.click()

        error = driver.find_element(By.XPATH, "//div[@class='error-message-container error']")
        self.assertEqual(error.text, "Epic sadface: Username and password do not match any user in this service")

    def test_login2(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        nom = driver.find_element(By.XPATH, "//input[@id='user-name']")
        password = driver.find_element(By.XPATH, "//input[@id='password']")
        boton = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("")
        password.send_keys("admin123")
        boton.click()

        error = driver.find_element(By.XPATH, "//div[@class='error-message-container error']")
        self.assertEqual(error.text, "Epic sadface: Username is required")

    def test_login3(self):
        driver = self.driver

        driver.get("https://www.saucedemo.com/")
        nom = driver.find_element(By.XPATH, "//input[@id='user-name']")
        password = driver.find_element(By.XPATH, "//input[@id='password']")
        boton = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("admin")
        password.send_keys("")
        boton.click()

        error = driver.find_element(By.XPATH, "//div[@class='error-message-container error']")
        self.assertEqual(error.text, "Epic sadface: Password is required")

    def test_login4(self):

        driver = self.driver

        driver.get("https://www.saucedemo.com/")
        nom = driver.find_element(By.XPATH, "//input[@id='user-name']")
        password = driver.find_element(By.XPATH, "//input[@id='password']")
        boton = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("standard_user")
        password.send_keys("secret_sauce")
        boton.click()

        product_title=driver.find_element(By.XPATH, "//span[@data-test='title']")
        self.assertEqual(product_title.text, "Products")

def tearDown(self):
    self.driver.quit()


if __name__ == '__main__':
    unittest.main()
