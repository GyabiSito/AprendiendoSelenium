# 🧩 Page Object Model (POM) con Selenium y Unittest

Este repositorio muestra cómo aplicar el patrón **Page Object Model (POM)** en pruebas automatizadas con Selenium.
El objetivo del POM es **separar la lógica de las pruebas** de las **acciones sobre la página**, haciendo el código más **limpio, reutilizable y fácil de mantener**.

---

## 📌 ¿Qué es el Page Object Model?

El **Page Object Model** es un patrón de diseño que consiste en:

1. **Clase de prueba (Test Case):** contiene solo la lógica de validación y flujo de pruebas.
2. **Clase de funciones (Page / Funciones):** contiene los métodos que interactúan con los elementos de la página (clicks, inputs, selects, validaciones, etc.).

De esta manera:

* Si cambian los elementos de la página, solo se modifica la clase de funciones.
* Las pruebas quedan más legibles y fáciles de mantener.

---

## ⚙️ Ejemplo de estructura con `unittest`

### Archivo `test_login.py`

```python
import time
import unittest
import sys
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Importamos la clase Funciones desde la carpeta correspondiente
CURRENT_DIR = Path(__file__).resolve().parent
FUNCIONES_DIR = CURRENT_DIR / "Funciones"
if str(FUNCIONES_DIR) not in sys.path:
    sys.path.insert(0, str(FUNCIONES_DIR))

from Funciones_Globales import Funciones

service = Service(r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
t = .3


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(t)

    def test_login(self):
        driver = self.driver
        f = Funciones(driver)

        f.Saludo()
        f.Navegar("https://www.saucedemo.com/")
        f.Texto_XPath("//input[@id='user-name']", "standard_user", t)
        f.Texto_XPath("//input[@id='password']", "secret_sauce", t)
        f.Texto_XPath_Valida("//input[@id='user-namafsde']", "standard_user222", t)
        f.Click_XPath_Valida("//input[@id='login-button']", t)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
```

### Archivo `Funciones.py`

```python
import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Funciones():
    def __init__(self, driver):
        self.driver = driver

    def Saludo(self):
        print("Hola")

    def Tiempo(self, tiempo):
        return time.sleep(tiempo)

    def Navegar(self, url):
        self.driver.get(url)

    def Texto_XPath(self, xpath, text, tiempo):
        elemento = self.driver.find_element(By.XPATH, xpath)
        elemento.clear()
        elemento.send_keys(text)
        time.sleep(tiempo)

    def Texto_XPath_Valida(self, xpath, text, tiempo):
        try:
            val = WebDriverWait(self.driver, tiempo).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.clear()
            val.send_keys(text)
            time.sleep(tiempo)
        except TimeoutException:
            print("El elemento no se encuentra")

    def Click_XPath_Valida(self, xpath, tiempo):
        try:
            val = WebDriverWait(self.driver, tiempo).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            time.sleep(tiempo)
        except TimeoutException:
            print("El elemento no se encuentra")

    # Otros métodos disponibles (Select, Upload, Check, etc.)
    # ...
```

---

## ✅ Beneficios del POM

* **Reutilización de código:** los métodos de la clase `Funciones` pueden usarse en múltiples pruebas.
* **Mantenibilidad:** si cambia un localizador (ej: un XPath), se actualiza solo en un lugar.
* **Legibilidad:** los test cases son más cortos y fáciles de entender.
* **Escalabilidad:** se pueden crear páginas específicas (ej. `LoginPage`, `ProductPage`) que hereden de `Funciones`.

---
