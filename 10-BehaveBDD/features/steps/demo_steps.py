from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Funciones_Globales.Funciones import Funciones

@given(u'Abriendo el navegador')
def step_impl(context):
    service = Service(r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
    context.driver = webdriver.Chrome(service=service)
    context.f = Funciones(context.driver)
    context.f.Navegar("https://demoqa.com/text-box")

@when(u'Cargando el nombre del "{nombre}"')
def step_impl(context, nombre):
    context.f.Texto_ID("userName", nombre, 1)

@then(u'Cargando su "{email}"')
def step_impl(context, email):
    context.f.Texto_ID("userEmail", email, 2)

@then(u'Cargando su nueva "{direccion}"')
def step_impl(context, direccion):
    context.f.Texto_ID("currentAddress", direccion, 2)
    context.driver.quit()
