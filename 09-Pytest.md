# 🧪 PyTest con Selenium

Este documento resume y explica todo lo que se vio en la práctica con **PyTest** aplicado a pruebas automatizadas en Selenium.

---

## 🔧 Instalación

```bash
pip install -U pytest
```

Verificar versión instalada:

```bash
pytest --version
```

---

## ▶️ Ejecución básica de tests

Ejemplo de ejecución sobre un archivo de pruebas `Login1.py`:

```bash
pytest Login1.py
```

Salida típica:

```
collected 4 items

Login1.py ....   [100%]
```

Cada `.` indica un test **PASSED**.

---

## 🔍 Modos de ejecución

* **Modo detallado (-v)**

```bash
pytest -v Login1.py
```

Muestra el nombre de cada test y su estado.

* **Modo con salida estándar (-s)**

```bash
pytest -s Login1.py
```

Permite ver los `print()` dentro de los tests.

* **Combinado (-s -v)**

```bash
pytest -s -v Login1.py
```

Muestra resultados detallados y también el contenido de `print()`.

---

## ⚙️ Setup y Teardown

PyTest permite definir funciones que se ejecutan **antes** y **después** de cada test:

```python
import pytest

def setup_function(function):
    print("\nSetup\n")

def teardown_function(function):
    print("\nTeardown\n")

def test_uno():
    print("Test 1")
```

📌 `setup_function` y `teardown_function` reciben como parámetro la función de test, porque son llamadas automáticamente por PyTest.

---

## 🏷️ Uso de marcas (Markers)

Se pueden marcar tests para agrupar o excluir:

```python
import pytest

@pytest.mark.run
def test_uno():
    print("Test uno")

@pytest.mark.notrun
def test_cuatro():
    print("Test cuatro")

@pytest.mark.skip
def test_siete():
    print("Test siete")
```

### Ejemplos de ejecución con marcas

* Ejecutar todos menos `cuatro`:

```bash
pytest -s -v -k "not cuatro"
```

* Ejecutar solo los que tengan la marca `run`:

```bash
pytest -s -v -k "run"
```

* Ejecutar todos excepto los con marca `run` y el `siete`:

```bash
pytest -s -v -k "not run and not siete"
```

---

## 🔁 Parametrización de tests

Permite ejecutar el mismo test con **diferentes datos**:

```python
import pytest

def get_Data():
    return [
        ("rodrigo", "1234"),
        ("juan", "1233234"),
        ("pedro", "12232334"),
        ("erika", "1234232"),
        ("carlos", "1234sdf"),
        ("Admin", "admin123")
    ]

@pytest.mark.parametrize("user,clave", get_Data())
def test_login(user, clave):
    print(f"Probando con usuario: {user}, clave: {clave}")
```

Resultado: se ejecuta `test_login` una vez por cada par usuario/clave.

---

## 🧩 Fixtures

Las **fixtures** permiten inicializar y limpiar recursos de forma más flexible que `setup/teardown`.

```python
import pytest

@pytest.fixture(scope='module')
def setup_login():
    print("Entrando al sistema")
    yield
    print("Saliendo del sistema")

@pytest.mark.usefixtures("setup_login")
def test_uno():
    print("Test con fixture")
```

### Alcances de fixture

* `function` → se ejecuta antes/después de cada test (default).
* `module` → se ejecuta una vez por archivo de tests.
* `class` → una vez por clase.
* `session` → una vez por toda la sesión de pruebas.

---

## 🌐 Ejemplos con Selenium

### Test simple de formulario

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()

driver.find_element(by="id", value="userName").send_keys("Jose")
driver.find_element(by="id", value="userEmail").send_keys("asd@gmail.com")
driver.find_element(by="id", value="currentAddress").send_keys("descripcion")
driver.find_element(by="id", value="permanentAddress").send_keys("direccion 2")

driver.execute_script("window.scrollTo(0, 500)")
driver.find_element(by="id", value="submit").click()

print(driver.title)
driver.close()
```

### Test con validación de error

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

error = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//li[contains(.,'The credentials provided are incorrect')]"))
)

assert error.text == "The credentials provided are incorrect"
```

---

## 📌 Resumen

* `pytest archivo.py` ejecuta todos los tests.
* `-s` muestra los `print()`.
* `-v` muestra detalles.
* `setup/teardown` inicializan y limpian antes/después de cada test.
* `@pytest.mark` permite filtrar o saltar tests.
* `@pytest.mark.parametrize` ejecuta un test con múltiples datos.
* `@pytest.fixture` ofrece un setup más avanzado y reutilizable.

Con estas herramientas, PyTest se convierte en un framework potente y flexible para pruebas automatizadas con Selenium 🚀
