import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from FuncionesPytest.Funciones import Funciones
t=.8


@pytest.fixture(scope='module')
def setup_Login():
    global driver, f
    service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f = Funciones(driver)
    f.Texto_Name("username", "Admin", t)
    f.Texto_Name("password", "admin123", t)
    f.Click_XPath_Valida("/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button", t)
    #print("Entrando al sistema")


def teardown_function():
    print("Fin de todos los Test")
    driver.close()

@pytest.mark.login
@pytest.mark.usefixtures("setup_Login")
def test_uno():
    etiqueta=driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
    print(etiqueta)
    if(etiqueta=="Dashboard"):
        print("Adentro")
        assert etiqueta=="Dashboard"

    else:
        print("Afuera")
        assert etiqueta=="Dashboa", "No estas en la pagina de inicio"


