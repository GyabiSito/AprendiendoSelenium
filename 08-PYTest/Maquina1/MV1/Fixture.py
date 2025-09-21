import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from FuncionesPytest.Funciones import Funciones
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

def setup_function(function):
    global driver
    global f
    service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://admin-demo.nopcommerce.com/login?returnurl=%2Fadmin%2F")
    driver.maximize_window()
    f=Funciones(driver)
    f.Texto_ID("Email", "admin@yourstore.com", 1)
    f.Texto_ID("Password", "admin", 1)
    f.Click_XPath_Valida("/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button", 1)

def teardown_function(function):
    driver.quit()

def test_uno():

    f.Click_XPath_Valida("//a[@href='#'][contains(.,'Catalog')]",1)
    f.Click_XPath_Valida("(//p[contains(.,'Products')])[1]",1)
    f.Texto_ID("SearchProductName", "Test Product", 1)
    f.Texto_ID("GoDirectlyToSku", "SKU", 1)


def test_dos():
    #driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    f.Click_XPath_Valida( "(//p[contains(.,'Catalog')])[1]")
    f.Click_XPath_Valida( "(//p[contains(.,'Products')])[1]")
    f.Click_XPath_Valida("//a[@href='/Admin/Product/Create']")
    f.Texto_XPath("//input[@id='Name']","Laptop Dell",.3)
    f.Texto_XPath("//textarea[contains(@id,'ShortDescription')]","Laptop modelo nuevo tipo dell",.3)
    f.Click_XPath_Valida("//span[@class='tox-mbtn__select-label'][contains(.,'File')]")
    f.Click_XPath_Valida("//div[@class='tox-collection__item-label'][contains(.,'New document')]")
    driver.switch_to.frame(0)
    #f.Texto_Mixto("id","tinymce","Descripción Larga",t)
    campo=driver.find_element(By.ID, "tinymce")
    campo.send_keys("Descripción Larga"+Keys.TAB+"34567")
    time.sleep(4)
    #f.Texto_Mixto("xpath","//input[contains(@id,'Sku')]","5464",t)
