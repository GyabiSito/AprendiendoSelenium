import time
import unittest
import sys
import os
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
CURRENT_DIR = Path(__file__).resolve().parent
FUNCIONES_DIR = CURRENT_DIR / "Funciones"
if str(FUNCIONES_DIR) not in sys.path:
    sys.path.insert(0, str(FUNCIONES_DIR))

from Funciones import Funciones

service = Service(r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
t = .3


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(t)
        driver=self.driver

    def test1(self):
        driver=self.driver
        f=Funciones(driver)
        f.Saludo()
        f.Navegar("https://www.saucedemo.com/")
        f.Texto_XPath("//input[@id='user-name']","standard_user",t)
        f.Texto_XPath("//input[@id='password']","secret_sauce",t)
        f.Texto_XPath_Valida("//input[@id='user-namafsde']","standard_user222",t)
        f.Click_XPath_Valida("//input[@id='login-button']",t)


    def tearDown(self):
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()
