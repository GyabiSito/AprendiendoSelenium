import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
t = 2


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(t)

    def test1(self):
        self.driver.get("https://demoqa.com/text-box")
        time.sleep(2)  

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
