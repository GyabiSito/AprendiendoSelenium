# 🧪 Pruebas automatizadas con Selenium y Unittest en Python

## ⚙️ Estructura básica de una prueba con `unittest`

Un test con Selenium y unittest se organiza en una **clase** que hereda de `unittest.TestCase`.
Se utilizan **métodos especiales**:

* `setUp()` → Se ejecuta antes de cada test (inicializa el navegador).
* `tearDown()` → Se ejecuta después de cada test (cierra el navegador).
* Los **métodos de prueba** deben comenzar con `test_`.

Ejemplo mínimo:

```python
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
t = 2

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(t)

    def test_open_demoqa(self):
        self.driver.get("https://demoqa.com/text-box")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
```

---

## 🧑‍💻 Ejemplo práctico: Pruebas de login en SauceDemo

Este ejemplo prueba diferentes escenarios de login en la página [SauceDemo](https://www.saucedemo.com/):

```python
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe")

class PruebaLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def test_login_invalido(self):
        """Usuario y contraseña incorrectos"""
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("admin")
        driver.find_element(By.ID, "password").send_keys("admin123")
        driver.find_element(By.ID, "login-button").click()
        error = driver.find_element(By.CLASS_NAME, "error-message-container")
        self.assertEqual(
            error.text,
            "Epic sadface: Username and password do not match any user in this service"
        )

    def test_username_vacio(self):
        """Campo usuario vacío"""
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "password").send_keys("admin123")
        driver.find_element(By.ID, "login-button").click()
        error = driver.find_element(By.CLASS_NAME, "error-message-container")
        self.assertEqual(error.text, "Epic sadface: Username is required")

    def test_password_vacio(self):
        """Campo password vacío"""
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("admin")
        driver.find_element(By.ID, "login-button").click()
        error = driver.find_element(By.CLASS_NAME, "error-message-container")
        self.assertEqual(error.text, "Epic sadface: Password is required")

    def test_login_exitoso(self):
        """Credenciales correctas"""
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        titulo = driver.find_element(By.XPATH, "//span[@data-test='title']")
        self.assertEqual(titulo.text, "Products")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
```

---

## 📌 Notas importantes

* Usa `self.driver.quit()` en lugar de `close()` para cerrar correctamente el navegador.
* Los métodos deben **empezar con `test_`** para que `unittest` los reconozca.
* Puedes ejecutar los tests con:

  ```bash
  python nombre_del_script.py
  ```
