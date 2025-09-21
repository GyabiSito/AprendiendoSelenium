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
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service

t = .8


@pytest.fixture(scope='module')
def setup_login_uno():
    global driver, f
    service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f = Funciones(driver)
    f.Texto_ID("Email", "admin@yourstore.com", t)
    f.Texto_ID("Password", "admin", t)
    f.Click_XPath_Valida("//button[@type='submit'][contains(.,'Log in')]", t)
    print("Entrando al sistema")
    yield
    print("Salida del login uno")
    driver.close()


@pytest.fixture(scope='module')
def setup_Login_dos():
    global driver, f
    service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f = Funciones(driver)
    service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f.Texto_Name("Username", "Admin", t)
    f.Texto_Name("password", "admin123", t)
    f.Click_ID_Valida( "btnLogin", t)
    print("Entrando al sistema")
    yield
    print("Salida del login uno")
    driver.close()


@pytest.mark.usefixtures("setup_login_uno")
def test_uno():
    print("Entrando el sistema uno")
    f.Click_XPath_Valida( "(//p[contains(.,'Customers')])[1]", t)
    f.Click_XPath_Valida( "(//p[contains(.,'Customers')])[2]", t)
    f.Texto_XPath( "//input[contains(@id,'SearchFirstName')]", "victoria", t)
    f.Click_XPath_Valida( "//button[contains(@id,'search-customers')]", t)
    # Creando un nuevo usuario
    f.Click_XPath_Valida( "//a[@href='/Admin/Customer/Create']", t)
    email = driver.find_element(By.XPATH, "//input[contains(@id,'Email')]")
    email.send_keys("juan@gmail.com" + Keys.TAB + "12345" + Keys.TAB + "Juan" + Keys.TAB + "Perez")
    time.sleep(3)
    f.Click_XPath_Valida( "//input[contains(@id,'Gender_Male')]", t)


@pytest.mark.usefixtures("setup_Login_dos")
def test_dos():
    print("Entrando el sistema dos")
    f.Click_XPath_Valida( "//b[contains(.,'Admin')]", t)
    f.Click_XPath_Valida( "//a[contains(@id,'menu_admin_UserManagement')]", t)
    f.Texto_ID( "//input[contains(@id,'searchSystemUser_userName')]", "ananya Dash", t)
    f.Click_XPath_Valida( "//input[contains(@id,'searchBtn')]", t)
    f.Click_XPath_Valida( "//input[contains(@id,'btnAdd')]", t)
    # f.Select_Xpath_Type("//select[contains(@id,'systemUser_userType')]", "index", 0, t)
