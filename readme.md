# 🧪as Selenium Testing en Python — Guía Completa

Bienvenido a este repositorio donde se documentan todas las prácticas y herramientas necesarias para automatizar pruebas
web usando **Python + Selenium**. Vas a encontrar desde lo más básico hasta patrones avanzados como **Page Object Model
**, manejo de Excel para DDT, entornos virtuales, y frameworks como `unittest`, `pytest` y `behave`.

> Este repo es parte de un curso/práctica personal para dominar Selenium con ejemplos claros, modularizados y
> actualizados. Dale que va.

---

## 📁 Estructura del contenido

| #   | Tema                                  | Archivo                      |
|-----|---------------------------------------|------------------------------|
| 1   | Introducción a Python                 | `01-Introduccion.md`         |
| 2   | Selectores (CSS / XPath)              | `02-Selectores.md`           |
| 3.1 | Ejemplos con Selenium                 | `03.1-Selenium.md`           |
| 3.2 | Expected Conditions + WebDriverWait   | `03.2-ExpectedConditions.md` |
| 4   | Tests con `unittest`                  | `04-Unitest.md`              |
| 5   | Page Object Model (POM)               | `05-PageObjectModel.md`      |
| 6   | Manejo de Excel (DDT)                 | `06-Excel.md`                |
| 7   | Entornos Virtuales + Pytest Paralelo  | `07-VEnv.md`                 |
| 8   | Mouse Actions avanzadas               | `08-Mouse Actions.md`        |
| 9   | Testing con `pytest`                  | `09-Pytest.md`               |
| 10  | Validaciones (`assert`, `assertpy`)   | `10-Assertions.md`           |
| 11  | Reportes con `pytest-html` y `Allure` | `11-Reports.md`              |
| 12  | BDD con `behave`                      | `12-Behave.md`               |
| -   | Prueba inicial / setup                | `00-prueba.md`               |

---

## 🚀 Tecnologías y Librerías

* [x] **Selenium WebDriver** (automatización web)
* [x] `unittest` y `pytest` (frameworks de testing)
* [x] `behave` (BDD con Gherkin)
* [x] `openpyxl` (manejo de Excel)
* [x] `assertpy` (soft assertions)
* [x] `pytest-xdist` (ejecución paralela)
* [x] `pytest-html` y `Allure` (reportes visuales)

---

## 📌 Temas destacados

### ✅ Selenium desde cero

* Cómo instalar Selenium
* Descargar drivers (Chrome/Firefox)
* Interacción con el DOM: inputs, botones, dropdowns
* Selectores: ID, CSS, XPath
* Navegación, scroll, waits y manejo de errores

### 🧺as Testing estructurado

* Tests simples con `unittest`
* Setup/TearDown
* Validaciones (`assertEqual`, `assert`)
* Pruebas con múltiples credenciales

### 🧹 Page Object Model (POM)

* Separación entre lógica de test y lógica de página
* Reutilización de métodos
* Clase `Funciones.py` con helpers
* Organización por carpetas

### 📄 Data Driven Testing (DDT)

* Leer/escribir archivos Excel
* Clase `Funexcel` con métodos útiles
* Integración con `pytest.mark.parametrize`

### ⚙️ Automatización Avanzada

* Mouse Actions: hover, doble click, drag & drop
* Subida de archivos
* Scroll dinámico con `scrollIntoView`
* Validación de modales, alerts, checkboxes

### 🧠 Expected Conditions

* Uso de `WebDriverWait` para esperas dinámicas
* `visibility_of_element_located`, `element_to_be_clickable`, etc.

### 🔬 Testing con `pytest`

* Markers personalizados
* Parametrización de tests
* Fixtures con diferentes scopes
* Soft assertions (`assertpy`)
* Reportes automáticos (`pytest-html`, `Allure`)

### 📘️ Testing BDD con `behave`

* Features en Gherkin
* Steps con Selenium
* Uso de `Scenario Outline` y `Examples`
* Backgrounds reutilizables

---

## 📊 Reportes

* **pytest-html**: ejecutá tus tests y generá HTML automáticamente

```bash
pytest test_login.py --html=report.html
```

* **Allure**:

    * Instalar: `pip install allure-pytest`
    * Descargar el binario
      desde: [https://repo.maven.apache.org/maven2/io/qameta/allure/](https://repo.maven.apache.org/maven2/io/qameta/allure/)
    * Agregar al `PATH`
    * Generar: `allure generate ./results -o ./report --clean`
    * Servir: `allure serve ./results`

---

## 🥪 Ejecutar tests

```bash
# Unittest
python -m unittest test_login.py

# Pytest
pytest -s -v

# Pytest en paralelo
pytest -n 4

# Behave
behave features/
```

---

## 🧼 Recomendaciones

* Usá `WebDriverWait` en lugar de `sleep()`
* Mantené tus localizadores simples y estables
* Modularizá lo más posible con helpers reutilizables
* Activá entornos virtuales para cada proyecto
* Preferí `pytest` o `behave` si querés escalar

---

## 📌 Recursos extra

* [Documentación Selenium](https://www.selenium.dev/documentation/)
* [Pytest](https://docs.pytest.org/)
* [Behave](https://behave.readthedocs.io/)
* [Openpyxl](https://openpyxl.readthedocs.io/en/stable/)
* [Allure Reports](https://docs.qameta.io/allure/)
* [assertpy GitHub](https://github.com/assertpy/assertpy)

---


## 📄 Conclusión

Este repositorio fue pensado como una caja de herramientas integral para dominar Selenium y sus frameworks complementarios en el mundo Python. Ya sea que estés empezando o quieras mejorar tu flujo de pruebas automatizadas, acá tenés ejemplos reales, modularización, buenas prácticas y tips aplicables a proyectos del mundo real.

La idea no es solo que "funcione", sino que puedas escalar, mantener y entender cada parte de tu suite de tests. Y como siempre digo: el mejor test es el que está tan bien hecho que nadie se da cuenta que existe... porque todo anda bien.

---

## ℹ️ Acerca del curso

Este trabajo se realizó siguiendo el curso impartido por IBM en Udemy, disponible en:
[Master: Selenium con Python Test Qa Automation](https://www.udemy.com/course/master-selenium-webdriver-python-test-qa-automation)

---

## 📬 Contacto

Para dudas o sugerencias, puedes contactarme a través de Linkedin:
[Jose Hernandez](https://www.linkedin.com/in/jose-gabriel-hernandez-512899251/)