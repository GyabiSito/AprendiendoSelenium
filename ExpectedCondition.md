# 📌 Guía rápida de Expected Conditions en Selenium

Las **Expected Conditions (EC)** son condiciones que Selenium puede "esperar" antes de continuar la ejecución de un test. Se usan junto con `WebDriverWait` para manejar tiempos de carga dinámicos y evitar errores como `NoSuchElementException`.

---

## 🔑 Uso básico

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ejemplo: esperar hasta 10s que aparezca un elemento
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@id='mensaje']"))
)
```

---

## 📋 Lista de Expected Conditions más comunes

| Expected Condition                                    | Qué hace                                                          | Cuándo usarla                                           |
| ----------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------- |
| **`presence_of_element_located(locator)`**            | Verifica que el elemento existe en el DOM (puede estar oculto).   | Cuando solo quieres confirmar que el elemento se cargó. |
| **`visibility_of_element_located(locator)`**          | El elemento está en el DOM **y es visible** (tamaño mayor a 0x0). | Cuando necesitas interactuar o leer el texto.           |
| **`element_to_be_clickable(locator)`**                | El elemento es visible y habilitado (clickeable).                 | Antes de hacer `click()` en botones o enlaces.          |
| **`text_to_be_present_in_element(locator, text)`**    | Espera a que un elemento contenga cierto texto.                   | Para validar mensajes dinámicos como "Login exitoso".   |
| **`invisibility_of_element(locator)`**                | Espera que un elemento desaparezca (del DOM o invisible).         | Para loaders o spinners que bloquean la página.         |
| **`title_is(title)`**                                 | El título de la página es exactamente el indicado.                | Después de redirecciones.                               |
| **`title_contains(text)`**                            | El título contiene un texto específico.                           | Más flexible que `title_is`.                            |
| **`alert_is_present()`**                              | Espera a que aparezca un popup nativo (`alert`).                  | Para manejar `alert.accept()` o `alert.dismiss()`.      |
| **`frame_to_be_available_and_switch_to_it(locator)`** | Espera que un `<iframe>` esté disponible y hace el switch.        | Para trabajar dentro de iframes.                        |
| **`element_to_be_selected(element)`**                 | Espera a que un checkbox o radio esté seleccionado.               | Validación de formularios.                              |

---

## ✅ Ejemplo práctico: mensaje de error visible

```python
error = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//li[contains(.,'The credentials provided are incorrect')]"))
)

assert error.text == "The credentials provided are incorrect"
```

Esto asegura que el mensaje de error **exista y sea visible** antes de validarlo.

---

## 🚀 Recomendación

Crea funciones de ayuda para reutilizar estas condiciones:

```python
def esperar_visible(driver, locator, tiempo=10):
    return WebDriverWait(driver, tiempo).until(
        EC.visibility_of_element_located(locator)
    )

def esperar_clickable(driver, locator, tiempo=10):
    return WebDriverWait(driver, tiempo).until(
        EC.element_to_be_clickable(locator)
    )
```

