# 📘 Introducción a Behave con Selenium

Este documento explica cómo usar **Behave** (framework BDD en Python) junto con Selenium para automatizar pruebas con un enfoque de **Desarrollo Guiado por Comportamiento**.

---

## 🔧 Instalación

1. Crear y activar un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

2. Instalar dependencias necesarias:

```bash
pip install behave selenium
```

---

## 📂 Estructura típica de un proyecto Behave

```
10-BehaveBDD (proyecto)/
│
├── features/
│   ├── demo.feature          # Archivo con escenarios en Gherkin
│   ├── steps/                # Carpeta de definición de pasos
│   │   └── demo_steps.py     # Implementación en Python de cada paso
│   └── environment.py        # Configuración opcional de hooks
└── Funciones_Globales/       # Librería auxiliar para Selenium
    └── Funciones.py
```

---

## 📝 Ejemplo de Feature (`features/demo.feature`)

```gherkin
Feature: Nuestro primer Demo

  Background:
    Given Abriendo el navegador

  Scenario Outline: Corriendo nuestro primer Test
      When Cargando el nombre del "<nombre>"
      Then Cargando su "<email>"
      Then Cargando su nueva "<direccion>"

      Examples:
        | nombre   | email              | direccion   |
        | nombre1  | email1@gmail.com   | direccion1  |
        | nombre2  | email2@gmail.com   | direccion2  |
        | nombre3  | email3@gmail.com   | direccion3  |
        | nombre4  | email4@gmail.com   | direccion4  |
        | nombre5  | email5@gmail.com   | direccion5  |
```

📌 Este archivo está escrito en **Gherkin**, legible para usuarios no técnicos.

---

## 🔨 Ejemplo de Steps (`features/steps/demo_steps.py`)

```python
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
```

📌 Cada paso (`Given`, `When`, `Then`) se enlaza con una función en Python.

---

## ⚡ Comandos útiles

* Ejecutar todos los escenarios:

```bash
behave
```

* Ejecutar un archivo `.feature` específico:

```bash
behave features/demo.feature
```

* Ejecutar un escenario con nombre:

```bash
behave -n "Corriendo nuestro primer Test"
```

---

## 🎯 Conceptos clave

* **Feature (.feature):** archivo en lenguaje **Gherkin** que describe funcionalidades legibles para negocio/usuarios.
* **Steps (.py):** implementación en Python que conecta cada línea Gherkin con Selenium.
* **Background:** pasos comunes que se ejecutan antes de cada escenario.
* **Scenario Outline + Examples:** permiten parametrizar un mismo escenario con múltiples datos.

---

## ✅ Resumen

1. Escribir el **feature** en Gherkin (legible por usuario).
2. Implementar los **steps** en Python usando Selenium.
3. Ejecutar con `behave` desde consola.
4. Usar **Background** para inicializar pasos comunes.
5. Usar **Scenario Outline** + **Examples** para probar con varios datos.

Con esto, Behave permite integrar **BDD + Selenium**, generando pruebas entendibles tanto para desarrolladores como para usuarios finales
