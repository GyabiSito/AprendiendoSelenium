import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from FuncionesPytest.Funciones import Funciones
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_invalido():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    f = Funciones(driver)
    f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    f.Texto_ID("Email", "admin@yourstore.com", 1)
    f.Texto_ID("Password", "1234", 1)
    f.Click_XPath_Valida("/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button", 1)
    # Espera hasta que aparezca el mensaje de error
    error = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[contains(.,'The credentials provided are incorrect')]"))
    )

    print(error.text)
    if (error.text == "The credentials provided are incorrect"):
        print("Prueba correcta")
    else:
        print("Prueba incorrecta")


def test_sin_correo():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    f = Funciones(driver)
    f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    f.Texto_ID("Email", "", 1)
    f.Texto_ID("Password", "1234", 1)
    f.Click_XPath_Valida("/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button", 1)
    error = driver.find_element(By.ID, "Email-error")
    if (error.text == "Please enter your email"):
        print("Prueba correcta")
    else:
        print("Prueba incorrecta")
    print(error.text)

def test_enter_valid_email():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    f = Funciones(driver)
    f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    f.Texto_ID("Email", "emailnovalido", 1)
    f.Texto_ID("Password", "1234", 1)
    f.Click_XPath_Valida("/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button", 1)
    error = driver.find_element(By.ID, "Email-error")
    if (error.text == "Please enter a valid email address."):
        print("Prueba correcta")
    else:
        print("Prueba incorrecta")
    print(error.text)

def test_login():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    f = Funciones(driver)
    f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    f.Texto_ID("Email", "admin@yourstore.com", 1)
    f.Texto_ID("Password", "admin", 1)
    f.Click_XPath_Valida("/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button", 1)
