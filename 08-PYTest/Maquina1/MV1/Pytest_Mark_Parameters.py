import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from FuncionesPytest.Funciones import Funciones
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
t=.8


def get_Data():
    return [
        ("rodrigo","1234"),
        ("juan", "1233234"),
        ("pedro", "12232334"),
        ("erika", "1234232"),
        ("carlos", "1234sdf"),
        ("Admin", "admin123")
    ]


@pytest.mark.login
@pytest.mark.parametrize("user,clave",get_Data())
def test_login(user,clave):
    global driver
    service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f = Funciones(driver)
    f.Texto_Name("username", user, t)
    f.Texto_Name("password", clave, t)
    f.Click_XPath_Valida("/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button", t)
    print("Entrando al sistema")


def teardown_function():
    print("Salida del test")
    driver.close()

