# 🧭 README: Ejemplos de Selenium (carpeta 03-Pruebas)

Este archivo muestra tres formas distintas de **seleccionar e interactuar con elementos** del DOM usando Selenium: `XPath`, `ID` y `CSS Selector`. Todas las versiones hacen lo mismo: completan el formulario en [https://demoqa.com/text-box](https://demoqa.com/text-box).

# Índice — README: Ejemplos de Selenium (carpeta 03-Pruebas)


1. [**Test_01, Test_02, Test_03 — Selectores**](#-test_01test_02test_03--selectores)
   * [Ejemplo 1: XPath](#-ejemplo-1-usando-xpath)
   * [Ejemplo 2: ID](#-ejemplo-2-usando-id-más-simple)
   * [Ejemplo 3: CSS Selectors](#-ejemplo-3-usando-css-selectors)
   * [Comparativa rápida](#-comparativa-rápida)

2. [**Test_04, Test_05 — Keys y Historial**](#-test_04test_05--keys-y-historial)
   * [Ejemplo 4: Uso de Keys](#-ejemplo-4-usando-keys-para-simular-teclado)
   * [Ejemplo 5: Navegación e historial](#-ejemplo-5-navegación-y-manejo-del-historial)

3. [**Test_06, Test_07 — Implicit vs Explicit Wait**](#-test_06-test_07--implicit-vs-explicit-wait-en-selenium)
   * [Implicit wait](#-ejemplo-con-implicitly_wait-implicit-wait)
   * [Explicit wait](#-ejemplo-con-webdriverwait-y-expected_conditions-explicit-wait)
   * [Comparación](#-comparación-de-esperas)

4. [**Test_08 — Checkbox e iFrame**](#-test_08--checkbox-e-iframe)

5. [**Test_09 — Dropdowns**](#-test_09--dropdowns)

6. [**Test_10 — Error Handling**](#-test_10--error-handling)

7. [**Test_11 — Subida de archivos**](#-test_11--subida-de-archivos)

8. [**Test_12 — Scroll con execute_script**](#-test_12--scroll-con-execute_script-y-scrollintoview-en-selenium)

9. [**Test_13 — Manejo de Links**](#-test_13--obtener-y-navegar-por-links)

10. [**Test_14 — Manejo de Modales**](#-test_14--manejo-de-modales-y-botones-en-selenium)

11. [**Test_15 — Verificación de Elementos (is_displayed)**](#-test_15--verificación-de-elementos-con-is_displayed-en-selenium)

---

## Conclusiones por sección (resumen ejecutivo)

* **Selectores (Test\_01–03):** Priorizar `ID` por simplicidad y performance; `CSS` para legibilidad; `XPath` para casos complejos. Mantener los selectores cortos y estables.
* **Keys e Historial (Test\_04–05):** Usar `Keys` para simular usuario real y `history.go()` para control fino de navegación. Útil en flujos de formularios.
* **Waits (Test\_06–07):** `Implicit` como base moderada; `Explicit` para condiciones puntuales. Evitar `sleep()` salvo debugging.
* **Checkbox + iFrame (Test\_08):** Siempre `switch_to.frame` antes de interactuar. Validar con `.is_selected()` para estados consistentes.
* **Dropdowns (Test\_09):** Usar `Select` con `visible_text` para claridad. En multi-select, recordar `deselect_*` para limpiar estado.
* **Error Handling (Test\_10):** Envolver cada test con `try/except/finally` y cerrar con `driver.quit()` para no dejar procesos colgados.
* **File Upload (Test\_11):** Subir con `.send_keys(ruta)` y esperar el input con `WebDriverWait`. No dependas del diálogo del SO.
* **Scroll (Test\_12):** Preferir `element.scrollIntoView()` sobre posiciones fijas; combinar con `WebDriverWait` para contenido lazy.
* **Links (Test\_13):** Enumerar con `find_elements('a')` y navegar con `LINK_TEXT`/`PARTIAL_LINK_TEXT`. Loguear `href` para depurar.
* **Modales (Test\_14):** Tratar modales HTML con `element_to_be_clickable`. Distinguirlos de alerts JS (`switch_to.alert`).
* **Visibilidad (Test\_15):** Verificar `is_displayed()` antes de interactuar; complementar con `is_enabled()`/`is_selected()`.


---


# 🧠 Mapa Mental — Selenium (README 03-Pruebas)

```
Selenium (03-Pruebas)
│
├── Selectores
│   ├── XPath → flexible, potente
│   ├── ID → simple, rápido
│   └── CSS Selector → limpio, performante
│
├── Keys & Navegación
│   ├── Keys.TAB, Keys.ENTER
│   └── Historial: back(), forward(), history.go()
│
├── Esperas
│   ├── Implicit Wait (global, todos los elementos)
│   ├── Explicit Wait (preciso, condiciones específicas)
│   └── Fluent Wait (configurable)
│
├── Elementos
│   ├── Checkboxes + iFrames
│   ├── Dropdowns (Select)
│   ├── Links
│   └── Scroll (scrollTo, scrollIntoView)
│
├── Manejo Avanzado
│   ├── Modales HTML
│   ├── Alerts JS (accept, dismiss, send_keys)
│   └── Subida de archivos (input[type=file])
│
├── Validaciones
│   ├── is_displayed()
│   ├── is_enabled()
│   └── is_selected()
│
└── Buenas Prácticas
    ├── try/except/finally
    ├── WebDriverWait en lugar de sleep()
    ├── driver.quit() para cerrar completo
    └── Modularización y rutas configurables
```

---

## 🔹 Contenido por secciones

1. **Selectores (Test\_01 a Test\_03)**

   * Diferentes formas de ubicar elementos: **XPath**, **ID** y **CSS Selector**.
   * Comparativa de pros y contras de cada estrategia.
   * Ejemplos de selectores avanzados.

2. **Keys y navegación (Test\_04 y Test\_05)**

   * Uso de `Keys` para simular teclado (`TAB`, `ENTER`).
   * Manejo del historial con `.back()`, `.forward()` y `execute_script`.

3. **Espera de elementos (Test\_06 y Test\_07)**

   * **Implicit Wait** (`implicitly_wait`): espera global para todos los elementos.
   * **Explicit Wait** (`WebDriverWait` + `expected_conditions`): esperas específicas y más precisas.
   * Comparación y mejores prácticas.

4. **Checkboxes e iFrames (Test\_08)**

   * Cómo interactuar con elementos dentro de un **iframe** usando `switch_to.frame()`.
   * Ejemplo de checkboxes y uso de `.is_selected()`.

5. **Dropdowns (Test\_09)**

   * Manejo de `<select>` con la clase `Select`.
   * Single Select y Multiple Select.
   * Métodos: `select_by_visible_text`, `value`, `index`, `deselect`.

6. **Manejo de errores (Test\_10)**

   * Estructura `try / except / finally`.
   * Uso de `driver.quit()` para cerrar el navegador de forma segura.

7. **Subida de archivos (Test\_11)**

   * Upload con `send_keys` en inputs de tipo `file`.
   * Espera con `WebDriverWait`.
   * Manejo de `TimeoutException`.

8. **Scroll (Test\_12)**

   * Scroll manual con `execute_script("window.scrollTo")`.
   * Scroll dinámico con `scrollIntoView()`.

9. **Links (Test\_13)**

   * Obtener todos los enlaces con `find_elements(By.TAG_NAME, "a")`.
   * Navegar usando `LINK_TEXT` y `PARTIAL_LINK_TEXT`.

10. **Modales (Test\_14)**

    * Manejo de **modales HTML**.
    * Espera de botones clickeables con `element_to_be_clickable`.
    * Diferencias con alerts nativos de JavaScript.

11. **Validaciones con `is_displayed` (Test\_15)**

    * Verificar si un elemento está visible.
    * Complementos: `is_enabled()` e `is_selected()`.

---


# 📑 Test_01,Test_02,Test_03 => Selectores

## 🧪 Ejemplo 1: Usando XPath

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)

nom = driver.find_element(by="xpath", value="//input[contains(@id,'userName')]")
nom.send_keys("Jose")
time.sleep(2)

driver.find_element(by="xpath", value="//input[contains(@id,'userEmail')]").send_keys("asd@gmail.com")
time.sleep(2)

driver.find_element(by="xpath", value="//textarea[contains(@id,'currentAddress')]").send_keys("descripcion")
time.sleep(2)

driver.find_element(by="xpath", value="//textarea[contains(@id,'permanentAddress')]").send_keys("direccion 2")
driver.execute_script("window.scrollTo(0, 500)")
time.sleep(2)

driver.find_element(by="xpath", value="//button[contains(@id,'submit')]").click()
time.sleep(5)

print(driver.title)
driver.close()
```

### 📝 ¿Por qué usar XPath?

* Ideal cuando no hay ID o clase única.
* Permite búsquedas más complejas: por texto, combinaciones de atributos, posiciones.

#### Otros ejemplos XPath:

```xpath
//button[@id='submit']
//input[@type='text']
//div[text()='Text box']
//span[contains(text(),'Links')]
//*[@id='userName' or @type='text']
```

---

## 🧪 Ejemplo 2: Usando ID (más simple)

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)

nom = driver.find_element(by="id", value="userName")
nom.send_keys("Jose")
time.sleep(2)

driver.find_element(by="id", value="userEmail").send_keys("asd@gmail.com")
time.sleep(2)

driver.find_element(by="id", value="currentAddress").send_keys("descripcion")
time.sleep(2)

driver.find_element(by="id", value="permanentAddress").send_keys("direccion 2")
driver.execute_script("window.scrollTo(0, 500)")
time.sleep(2)

driver.find_element(by="id", value="submit").click()
time.sleep(5)

print(driver.title)
driver.close()
```

### ¿Por qué usar ID?

* Es la forma **más rápida y eficiente** si el elemento tiene un `id` único.
* Menos propenso a errores.

---

## 🧪 Ejemplo 3: Usando CSS Selectors

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)

nom = driver.find_element(By.CSS_SELECTOR, "#userName")
nom.send_keys("Jose")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "#userEmail").send_keys("asd@gmail.com")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "#currentAddress").send_keys("descripcion")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "#permanentAddress").send_keys("direccion 2")
driver.execute_script("window.scrollTo(0, 500)")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "#submit").click()
time.sleep(5)

print(driver.title)
driver.close()
```

### 📝 ¿Por qué usar CSS Selectors?

* Similar a cómo se escriben selectores en CSS (HTML).
* Muy performante.
* Más legible en casos simples.

#### Ejemplos de selectores CSS:

```css
input#userName
input[type='text']
div.container > input
button.submit-btn
```

---

## 🧠 Comparativa rápida

| Selector     | Uso               | Pros                   | Contras                    |
| ------------ | ----------------- | ---------------------- | -------------------------- |
| ID           | `by="id"`         | Rápido y simple        | Solo si hay ID único       |
| XPath        | `by="xpath"`      | Muy potente y flexible | Más difícil de mantener    |
| CSS Selector | `By.CSS_SELECTOR` | Similar a HTML/CSS     | No permite lógica compleja |

---

## 🔎 Referencia: `find_element`

```python
find_element(by=By.ID, value="element_id")
find_element(by=By.NAME, value="name")
find_element(by=By.CLASS_NAME, value="class")
find_element(by=By.TAG_NAME, value="input")
find_element(by=By.LINK_TEXT, value="Texto del enlace")
find_element(by=By.PARTIAL_LINK_TEXT, value="parte del texto")
find_element(by=By.XPATH, value="//div[@id='main']")
find_element(by=By.CSS_SELECTOR, value="div#main")
```

---

## 📌 Recomendaciones

* Empezá por `ID`. Si no hay, probá con `CSS`. Si necesitás lógica avanzada, andá a `XPath`.
* Evitá usar `sleep()` cuando sea posible. Mejor usar `WebDriverWait` y `expected_conditions`.
* Si estás scrapeando o automatizando procesos con muchos elementos similares, pensá bien tu estrategia de selectores.

---

# 📑 Test_04,Test_05 => Keys y historial

Este documento expande el README anterior con ejemplos extra de selectores, interacción con teclado y navegación entre páginas.

---

## 🧪 Ejemplo 4: Usando `Keys` para simular teclado

```python
from selenium.webdriver.common.keys import Keys

nom = driver.find_element(By.CSS_SELECTOR, "#userName")
nom.send_keys("Jose")
time.sleep(2)

nom.send_keys(
    Keys.TAB + "jose@gmail.com" +
    Keys.TAB + "Direccion 1" +
    Keys.TAB + "Direccion 2" +
    Keys.TAB + Keys.ENTER
)

driver.find_element(
    by=By.XPATH,
    value="//li[@class='btn btn-light '][contains(.,'Check Box')]"
).click()
```

👉 Con `Keys.TAB` movemos el foco entre campos como si fuéramos un usuario real, y con `Keys.ENTER` enviamos el formulario.

---

## 🧪 Ejemplo 5: Navegación y manejo del historial

```python
driver.get("https://demoqa.com/text-box")
driver.get("https://www.selenium.dev/documentation/webdriver/elements/finders/")
driver.get("https://github.com/nccgroup/VCG")

# Retroceder en el historial
driver.back()

# Alternativa con JavaScript
driver.execute_script("window.history.go(-1)")

# Avanzar en el historial
driver.forward()

# O bien avanzar 2 pasos con JavaScript
driver.execute_script("window.history.go(2)")
```

👉 Podés usar `.back()` y `.forward()`, pero con `execute_script("window.history.go()")` tenés más control.

---

## 📌 Recomendaciones

1. **Simulá usuarios reales** con `Keys` (`TAB`, `ENTER`, `ESC`) para testear formularios como si alguien estuviera tipeando.
2. **Controlá el historial** con `.back()`, `.forward()` o JavaScript según necesites.
3. **Combiná selectores**: empezá por `ID`, después `CSS`, y dejá `XPath` para búsquedas complejas.
4. **Evitá `sleep()`** cuando sea posible, preferí `WebDriverWait` y `expected_conditions` para sincronizar.

---

# 📑 Test_06, Test_07 => Implicit vs Explicit Wait en Selenium

Cuando automatizamos con Selenium, **los elementos no siempre cargan al instante**. Para evitar errores como `NoSuchElementException`, usamos técnicas de *wait* (esperas). Las dos más usadas son **implicit wait** y **explicit wait**.

---

## 🧪 Ejemplo con `implicitly_wait` (Implicit Wait)

```python
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()

# ⏳ Espera implícita (máximo 15 segundos)
driver.implicitly_wait(15)

nom = driver.find_element(by="xpath", value="//input[contains(@id,'userName')]")
nom.send_keys("Jose")

driver.find_element(by="xpath", value="//input[contains(@id,'userEmail')]").send_keys("asd@gmail.com")
driver.find_element(by="xpath", value="//textarea[contains(@id,'currentAddress')]").send_keys("descripcion")
driver.find_element(by="xpath", value="//textarea[contains(@id,'permanentAddress')]").send_keys("direccion 2")

# Scroll para ver el botón
driver.execute_script("window.scrollTo(0, 500)")
driver.find_element(by="xpath", value="//button[contains(@id,'submit')]").click()

time.sleep(1)
driver.close()
```

### 📌 ¿Qué hace `implicitly_wait`?

* Le da a Selenium un **tiempo máximo de espera** para encontrar cada elemento.
* Si encuentra el elemento antes, sigue sin esperar.
* Aplica a **todos los elementos** en la sesión.

👉 Es útil cuando los tiempos de carga son variables en toda la aplicación.

---

## 🧪 Ejemplo con `WebDriverWait` y `expected_conditions` (Explicit Wait)

```python
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Página local con un modal
driver.get("file:///C:/Users/Josec/OneDrive/Escritorio/Selenium/03-Pruebas/modal.html")
driver.maximize_window()

# Espera implícita global (15 seg máx)
driver.implicitly_wait(15)

# ✅ Espera explícita: hasta 10 seg hasta que aparezca el modal
modal = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "myModal"))
)

# Cerramos el modal
close_btn = modal.find_element(By.CSS_SELECTOR, "button.close")
close_btn.click()

# Rellenamos el formulario
driver.find_element(By.ID, "nombre").send_keys("Juan Pérez")
driver.find_element(By.ID, "email").send_keys("juan@example.com")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Pausa breve para ver el resultado
time.sleep(3)
driver.close()
```

### 📌 ¿Qué hace `WebDriverWait`?

* Espera hasta que se cumpla una condición específica (ejemplo: que un modal sea visible).
* Si la condición se cumple antes, sigue sin esperar más.
* Si no se cumple en el tiempo dado, lanza excepción.

#### 🔎 Ejemplos comunes de `expected_conditions`:

```python
EC.presence_of_element_located((By.ID, "elemento"))
EC.visibility_of_element_located((By.CSS_SELECTOR, "#btnEnviar"))
EC.element_to_be_clickable((By.XPATH, "//button[@id='submit']"))
EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Bienvenido")
EC.alert_is_present()
```

---

## 🧠 Comparación de esperas

* **Implicit Wait**: aplica a todos los elementos, es global, más general.
* **Explicit Wait**: se aplica a condiciones específicas, más preciso.
* **Fluent Wait**: como explicit, pero configurable con intervalos y excepciones.

---

## 📌 Recomendaciones

1. **Usá `implicitly_wait`** como base general, pero no abuses: puede ralentizar tests largos.
2. **Usá `explicit wait`** cuando un elemento cambie estado (ejemplo: un modal que aparece o un botón que se habilita).
3. **Combiná implicit + explicit wait**: implicit para lo básico, explicit para casos puntuales.
4. **Evitá `time.sleep()`** salvo en pruebas rápidas o debugging.
5. **Pensá como un usuario real**: esperá a que el elemento esté listo, no solo a que pasen X segundos.



# 📑 Test_08 => Checkbox e iFrame

En muchos sitios web, el contenido se renderiza dentro de un **iframe**. Para que Selenium pueda interactuar con los elementos internos, primero hay que hacer un `switch_to.frame()`.

En este ejemplo usamos la página de **W3Schools** para probar checkboxes.

---

## 🧪 Ejemplo: Checkboxes dentro de un iframe

```python
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

t = 1

service = Service(r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Página con ejemplo de checkboxes
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox")
driver.maximize_window()

# ✅ Cambiamos al iframe que contiene el formulario
driver.switch_to.frame("iframeResult")

# Seleccionamos el checkbox 1
chk1 = driver.find_element(By.ID, "vehicle1")
chk1.click()
time.sleep(t)

# Seleccionamos el checkbox 3
chk3 = driver.find_element(By.ID, "vehicle3")
chk3.click()
time.sleep(t)

# Hacemos click en Submit
sub = driver.find_element(By.XPATH, "//input[@type='submit']")
sub.click()
time.sleep(t)

driver.close()
```

---

## 📌 Puntos clave

1. **Uso de `iframe`**: antes de interactuar con un elemento dentro de un iframe, hay que hacer:

   ```python
   driver.switch_to.frame("iframeResult")
   ```

   Si no lo hacés, Selenium no encuentra los elementos.

2. **Checkboxes en Selenium**:

   * `.click()` marca o desmarca el checkbox.
   * Podés verificar si está seleccionado con `.is_selected()`.

   ```python
   chk1 = driver.find_element(By.ID, "vehicle1")
   if not chk1.is_selected():
       chk1.click()
   ```

3. **Submit en formularios**: se puede hacer `.click()` en el botón o usar `.submit()` desde cualquier elemento del form.

---

## 🚀 Recomendaciones

* Siempre revisá si tu elemento está dentro de un `iframe` o `shadow DOM`.
* Para checkboxes múltiples, podés recorrerlos con `find_elements`.
* Evitá `time.sleep()` cuando sea posible: usá `WebDriverWait` para esperar que el iframe o el checkbox estén listos.

---

# 📑 Test_09 => Dropdowns

En Selenium, los dropdowns (`<select>`) se manejan con la clase `Select` del módulo `selenium.webdriver.support.ui`. Acá te muestro cómo trabajar tanto con **single select** como con **multi select**.

---

## 🧪 Ejemplo con **Single Select Dropdown**

```python
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

service = Service(r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("file:///C:/Users/TuUsuario/Desktop/select_test.html")
driver.maximize_window()

# Localizamos el select
dropdown = Select(driver.find_element(By.ID, "select-demo"))

# Seleccionar por texto visible
dropdown.select_by_visible_text("Monday")
time.sleep(1)

# Seleccionar por value
dropdown.select_by_value("Friday")
time.sleep(1)

# Seleccionar por índice (0 = primera opción)
dropdown.select_by_index(3)  # Wednesday
time.sleep(1)

driver.close()
```

---

## 🧪 Ejemplo con **Multiple Select Dropdown**

```python
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

service = Service(r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("file:///C:/Users/TuUsuario/Desktop/select_test.html")
driver.maximize_window()

# Localizamos el multi-select
multi_dropdown = Select(driver.find_element(By.ID, "multi-select"))

# Seleccionar múltiples opciones
multi_dropdown.select_by_visible_text("Florida")
multi_dropdown.select_by_value("Texas")
multi_dropdown.select_by_index(2)  # New Jersey
time.sleep(2)

# Deseleccionar una opción
multi_dropdown.deselect_by_visible_text("Texas")
time.sleep(1)

# Deseleccionar todas
multi_dropdown.deselect_all()
time.sleep(1)

driver.close()
```

---

## 📌 Puntos Clave

1. **Clase `Select`**
   Necesaria para trabajar con `<select>` en Selenium:

   ```python
   from selenium.webdriver.support.ui import Select
   ```

2. **Métodos útiles**:

   * `select_by_visible_text("Texto")`
   * `select_by_value("valor")`
   * `select_by_index(n)`
   * `deselect_by_visible_text("Texto")`
   * `deselect_all()`

3. **Iterar todas las opciones**:

   ```python
   for option in multi_dropdown.options:
       print(option.text)
   ```

---

## 🚀 Recomendaciones

* Usá `select_by_visible_text` cuando quieras ser explícito con el usuario.
* `select_by_value` es más estable si trabajás con valores únicos en el HTML.
* En **multi-select**, recordá deseleccionar para no dejar estados sucios.
* Evitá `time.sleep()`, mejor usá `WebDriverWait` cuando los selects dependan de carga dinámica.

---


# 📑 Test_10 => Error Handling

Cuando automatizamos con Selenium, es buena práctica envolver el código en un bloque `try/except/finally` para capturar errores y asegurarnos de que el navegador se cierre siempre, aunque algo falle.

---

## 🧪 Ejemplo con `try/except/finally`

```python
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

t = 1

try:
    service = Service(r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("file:///C:/Users/Josec/OneDrive/Escritorio/Selenium/03-Pruebas/select.html")
    driver.maximize_window()

    # Dropdown simple
    select1 = driver.find_element(By.XPATH, "//select[contains(@id,'select-demo')]")
    dias = Select(select1)
    dias.select_by_visible_text("Sunday")
    time.sleep(t)

    dias.select_by_index(2)
    time.sleep(t)

    dias.select_by_value("Thursday")
    time.sleep(t)

    # Dropdown múltiple
    ciudad = Select(driver.find_element(By.ID, "multi-select"))
    ciudad.select_by_value("California")
    time.sleep(t)
    ciudad.select_by_value("New York")
    time.sleep(t)
    ciudad.select_by_index(2)
    time.sleep(t)

except Exception as e:
    print(f"❌ Error durante la ejecución: {e}")

finally:
    # Asegura cerrar el navegador siempre
    driver.quit()
```

---

## 📌 Puntos clave

1. **`try`**: bloque principal donde corre tu automatización.
2. **`except`**: captura cualquier error y lo muestra en consola.
3. **`finally`**: se ejecuta siempre, haya error o no, asegurando que el navegador se cierre con `driver.quit()`.

---

## 📌 Recomendaciones

* Siempre usá `driver.quit()` en lugar de `driver.close()`: cierra todo el proceso del navegador.
* Podés usar `logging` en lugar de `print` para registrar errores en un archivo.
* En proyectos grandes, envolvé cada **test case** en un `try/except` para aislar fallos y no frenar toda la suite.

---



# 📑 Test_11 => Subida de archivos

En este ejemplo usamos Selenium para **subir un archivo** en un formulario web. Además, aplicamos `WebDriverWait` para esperar al input de tipo `file` y un `try/except` para manejar errores con `TimeoutException`.

---

## 🧪 Ejemplo: Subida de archivo con `send_keys`

```python
import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

t = 1

service = Service(r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://testpages.herokuapp.com/styled/file-upload-test.html")
driver.maximize_window()
time.sleep(t)

try:
    # Esperamos hasta 5 segundos a que aparezca el input de file
    Buscar = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'fileinput')]"))
    )

    # Localizamos el input y subimos el archivo
    Buscar = driver.find_element("xpath", "//input[contains(@id,'fileinput')]")
    Buscar.send_keys("C:\\Users\\Josec\\OneDrive\\Escritorio\\Gh6Z6DUWQAEZZQu.jpg")
    time.sleep(t)

    # Marcamos el checkbox de imagen
    driver.find_element("xpath", "//input[contains(@id,'itsanimage')]").click()

    # Hacemos click en submit
    driver.find_element("xpath", "//input[contains(@type,'submit')]").click()
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("❌ El elemento no está disponible en el tiempo esperado")

finally:
    time.sleep(t)
    driver.close()
```

---

## 📌 Puntos clave

1. **Subida de archivos en Selenium**:

   * Se hace con `.send_keys("ruta_al_archivo")` en un input `type="file"`.
   * No se usan diálogos del sistema operativo, Selenium interactúa directo con el DOM.

2. **`WebDriverWait` + `expected_conditions`**:

   * Aseguramos que el input esté visible antes de usarlo.
   * En este caso, `visibility_of_element_located`.

3. **Manejo de excepciones**:

   * Capturamos `TimeoutException` para detectar si el elemento no apareció a tiempo.
   * Usamos `finally` para cerrar siempre el navegador.

---

## 📌 Recomendaciones

* Siempre usá `WebDriverWait` antes de interactuar con inputs de archivo (pueden tardar en cargar).
* Evitá hardcodear `time.sleep()`, solo usalo como apoyo visual durante el testing.
* Si el sitio valida extensiones, probá diferentes formatos de archivo en tus tests.
* Guardá rutas de archivos en variables de configuración para no ensuciar el código.

---


# 📑 Test_12 => Scroll con `execute_script` y `scrollIntoView` en Selenium

En algunos sitios web, los elementos no son visibles hasta que se hace **scroll**. Selenium no scrollea automáticamente, por lo que debemos usar **JavaScript** (`execute_script`) para llevar el elemento a la vista.

Este ejemplo usa **Pixabay** y busca el botón `Descubre más`.

---

## 🧪 Ejemplo: `scrollIntoView()` con WebDriverWait

```python
import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

t = 1

service = Service(r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://pixabay.com/es/")
driver.maximize_window()
time.sleep(t)

try:
    # Esperamos hasta 5 segundos a que aparezca el link "Descubre más"
    Buscar = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@href='/es/images/search/?order=ec'][contains(.,'Descubre más')]"))
    )

    # Scroll hacia el elemento
    driver.execute_script("arguments[0].scrollIntoView();", Buscar)
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("❌ El elemento no está disponible")

finally:
    time.sleep(t)
    driver.close()
```

---

## 📌 Puntos clave

1. **`scrollIntoView()`**

   * `driver.execute_script("arguments[0].scrollIntoView();", elemento)`
   * Hace scroll hasta que el elemento esté visible en la ventana.

2. **Alternativa: scroll manual**

   ```python
   driver.execute_script("window.scrollTo(0, 1500)")
   ```

   Útil para scrollear a posiciones fijas (no dinámicas).

3. **`WebDriverWait` + `expected_conditions`**

   * Garantiza que el elemento esté en el DOM antes de intentar hacer scroll.

---

## 📌 Recomendaciones

* Siempre preferí `scrollIntoView` sobre scroll fijo para asegurar que el elemento quede visible.
* Usá `WebDriverWait` antes de scrollear para evitar errores si el elemento aún no cargó.
* Si el sitio carga elementos con *infinite scroll*, combiná `scrollTo()` en bucle con verificaciones dinámicas.

---

## 📑 Test_13 => Obtener y navegar por links

En Selenium podemos **obtener todos los enlaces de una página** y navegar a través de ellos usando `find_elements` y `find_element` con estrategias como `By.TAG_NAME` y `By.LINK_TEXT`.

Este ejemplo utiliza un archivo HTML local con múltiples links.

---

## 🧪 Ejemplo: Obtener y navegar por links

```python
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

t = 1

service = Service(r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("file:///C:/Users/Josec/OneDrive/Escritorio/Selenium/03-Pruebas/links.html")
driver.maximize_window()
time.sleep(t)

# Obteniendo todos los links de la página
links = driver.find_elements(By.TAG_NAME, "a")
print("El número de Links que hay en la página es: ", len(links))

# Mostramos el texto de cada link
for num in links:
    print(num.text)

# Navegamos usando el texto exacto del enlace
driver.find_element(By.LINK_TEXT, "Date pickers").click()
time.sleep(t)

# Otro click en un sublink
driver.find_element(By.LINK_TEXT, "JQuery Date Picker").click()
time.sleep(t)

driver.close()
```

---

## 📌 Puntos clave

1. **Obtener todos los links**:

   ```python
   links = driver.find_elements(By.TAG_NAME, "a")
   for link in links:
       print(link.text)
   ```

   Esto devuelve una lista de todos los elementos `<a>` en la página.

2. **Navegar con `LINK_TEXT`**:

   ```python
   driver.find_element(By.LINK_TEXT, "Texto del link").click()
   ```

   Usa el texto visible del enlace.

3. **Navegar con `PARTIAL_LINK_TEXT`**:

   ```python
   driver.find_element(By.PARTIAL_LINK_TEXT, "Date").click()
   ```

   Útil cuando no conocés el texto completo del enlace.

---

## 📌 Recomendaciones

* Siempre verificá que los links estén visibles antes de hacer click (`WebDriverWait` + `expected_conditions`).
* Si tenés muchos enlaces dinámicos, usá `find_elements` y filtrá por atributos como `href`.
* Para depurar, imprimí `link.get_attribute("href")` además de `link.text`.
* Evitá depender únicamente del texto del link si la página cambia de idioma o localización.

---


# 📑 Test_14 => Manejo de Modales y Botones en Selenium

En Selenium, además de los *JavaScript alerts* tradicionales (`alert`, `confirm`, `prompt`), muchas páginas modernas usan **modales** (ventanas emergentes dentro del HTML). Para interactuar con ellos necesitamos esperar que sus botones sean **clickeables**.

Este ejemplo usa un modal con un botón **"Save changes"**.

---

## 🧪 Ejemplo: Modal con `WebDriverWait`

```python
import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

t = 2

service = Service(r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("file:///C:/Users/Josec/OneDrive/Escritorio/Selenium/03-Pruebas/alerts.html")
driver.maximize_window()
time.sleep(t)

# Abrimos el modal
driver.find_element(By.XPATH, "//a[@href='#myModal0']").click()
time.sleep(t)

# Esperar a que el botón "Save changes" sea clickeable
try:
    boton_save = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "(//a[@href='#'][contains(.,'Save changes')])[1]"))
    )
    boton_save.click()
    print("Botón 'Save changes' clickeado con éxito.")
    time.sleep(t)

except TimeoutException as ex:
    print("Error: El botón no estuvo disponible a tiempo.", ex.msg)

time.sleep(3)
driver.close()
```

---

## 📌 Puntos clave

1. **Abrir modal**:

   ```python
   driver.find_element(By.XPATH, "//a[@href='#myModal0']").click()
   ```

2. **Esperar botón clickeable**:

   ```python
   boton_save = WebDriverWait(driver, 5).until(
       EC.element_to_be_clickable((By.XPATH, "(//a[@href='#'][contains(.,'Save changes')])[1]"))
   )
   boton_save.click()
   ```

3. **Manejo de excepciones**:

   * Si el botón no aparece en el tiempo esperado, capturamos `TimeoutException`.

---

## 📌 Recomendaciones

* Usá `WebDriverWait` + `expected_conditions.element_to_be_clickable` para asegurar que el botón realmente pueda clickease.
* Diferenciá entre **modales HTML** (como este) y **alerts nativos de JS**, que se manejan con:

  ```python
  alert = driver.switch_to.alert
  alert.accept()   # Aceptar
  alert.dismiss()  # Cancelar
  alert.send_keys("texto")  # Enviar texto si es un prompt
  ```
* En pruebas reales, verificá también los **cambios en la UI** después de cerrar el modal.

---





## 📑 Test_15 => Verificación de Elementos con `is_displayed()` en Selenium

En Selenium, muchas veces necesitamos comprobar si un elemento **existe y está visible** antes de interactuar con él. Para esto utilizamos el método `is_displayed()`.

Este ejemplo usa la página principal de **DemoQA**.

---

## 🧪 Ejemplo: Comprobando si un elemento está visible

```python
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
t = 2

driver.get("https://demoqa.com/")
driver.maximize_window()

# Localizamos la imagen del logo
titulo = driver.find_element(By.XPATH, "//img[@src='/images/Toolsqa.jpg']")
print(titulo.is_displayed())  # Devuelve True o False

# Localizamos el primer cardtn1 = driver.find_element(By.XPATH, "(//div[contains(@class,'card-up')])[1]")

# Validamos si el título está visible
if titulo.is_displayed():
    print("✅ Existe la imagen")
    btn1.click()
    time.sleep(2)
else:
    print("❌ No existe la imagen")


time.sleep(2)
driver.close()
```

---

## 📌 Puntos clave

1. **`is_displayed()`**

   * Retorna `True` si el elemento está visible en la página.
   * Retorna `False` si el elemento existe en el DOM pero está oculto (ejemplo: con `display:none`).

2. **Uso en condicionales**

   ```python
   if elemento.is_displayed():
       print("El elemento es visible")
   else:
       print("El elemento NO es visible")
   ```

3. **Combinación con `is_enabled()` e `is_selected()`**

   * `is_enabled()`: comprueba si el elemento está habilitado para interactuar.
   * `is_selected()`: útil en checkboxes y radios para verificar si están seleccionados.

---

## 🚀 Recomendaciones

* Siempre usá `is_displayed()` antes de interactuar con elementos que pueden estar ocultos dinámicamente.
* En formularios dinámicos, combiná con `WebDriverWait` para esperar a que el elemento se vuelva visible.
* Si necesitás verificar múltiples estados, combiná `is_displayed()`, `is_enabled()` y `is_selected()` para mayor robustez.

---


# 📋 Resumen — README Selenium (03-Pruebas)

Este README recopila ejemplos prácticos de **automatización con Selenium en Python**, organizados en **15 tests**. Cada test cubre un caso de uso distinto, desde selectores básicos hasta manejo de modales, waits, iframes, uploads y validaciones de estado de elementos.

---

# 📌 Conclusión detallada

Este README funciona como un **mini-curso práctico de Selenium en Python**. A través de 15 tests progresivos, muestra cómo pasar de lo más básico (selectores e interacción con formularios) hasta escenarios más avanzados (esperas, iFrames, uploads, modales y validaciones de estado).

La estructura no solo enseña “cómo” hacer las cosas, sino también **cuándo conviene cada técnica**:

* **Selectores:** ID siempre que exista, CSS cuando se requiere legibilidad, XPath para búsquedas complejas.
* **Sincronización:** evitar depender de `time.sleep()`, priorizando `WebDriverWait`.
* **Robustez:** validar estados (`is_displayed`, `is_enabled`, `is_selected`) antes de actuar.
* **Mantenibilidad:** manejar errores con `try/except/finally`, usar `driver.quit()` y parametrizar rutas de archivos.
* **Realismo:** simular la interacción de un usuario real con `Keys`, scroll y manejo de modales.

En conjunto, este README no es solo una **colección de ejemplos aislados**, sino un **manual práctico y escalonado** para aprender Selenium de forma sólida, aplicable tanto a *web scraping* como a *test automation*.

Al finalizarlo, se obtiene una visión completa de cómo **diseñar pruebas automatizadas robustas, limpias y fáciles de mantener**, que es el objetivo principal de cualquier framework de automatización.
