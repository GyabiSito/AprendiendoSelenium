import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from FuncionesPytest.Funciones import Funciones
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="module")
def setup_login_uno():
    print("Empezando Login de Sistema")
    yield
    print("Saliendo de las pruebas login 1")

@pytest.fixture(scope="module")
def setup_login_dos():
    print("Empezando Login de Sistema 2")
    yield
    print("Saliendo de las pruebas login 2")

def test_uno(setup_login_uno):
    print("###########Empezando als pruebas del test 1########")

def test_dos(setup_login_dos):
    print("###########Empezando als pruebas del test 2########")

@pytest.mark.usefixtures("setup_login_dos")
def test_tres():
    print("###########Empezando als pruebas del test 3########")