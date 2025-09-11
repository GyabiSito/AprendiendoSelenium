## 🎯 Selectores CSS y XPath en Selenium

Cuando trabajamos con Selenium, **necesitamos seleccionar elementos del DOM de forma precisa**. Para eso usamos **selectores**, que pueden ser **CSS** o **XPath**. Son fundamentales para interactuar con formularios, botones, inputs, etc.

---

### 🧼 ¿Qué es un selector?

Un selector es una forma de decirle a Selenium: “Buscá este elemento, y no los otros”. Muy útil cuando hay muchos elementos similares (por ejemplo, 3 botones y querés hacer click en el segundo).

---

## 🔹 Selectores CSS

Los selectores CSS funcionan igual que en HTML/CSS.

### 📌 Sintaxis común:

* `#id` → Selecciona por ID
* `.clase` → Selecciona por clase
* `etiqueta` → Selecciona por etiqueta (por ejemplo, `input`, `button`, `div`)
* `etiqueta[atributo='valor']` → Selecciona por atributo
* `etiqueta.clase` → Selecciona etiqueta con clase específica
* `etiqueta#id` → Etiqueta con ID específico

### ✅ Ejemplos:

```css
input#userName                 # input con id="userName"
input[type='text']             # input donde type='text'
button.submit-btn              # botón con clase submit-btn
form input[name='email']       # input dentro de form donde name='email'
```

Podés usarlos en Selenium así:

```python
driver.find_element(By.CSS_SELECTOR, "input#userName")
```

---

## 🔹 XPath

XPath es más potente que CSS y permite navegar la estructura del DOM como si fuera un árbol.

### 📌 Sintaxis común:

* `//etiqueta` → Todos los elementos con esa etiqueta
* `//*[@atributo='valor']` → Cualquier etiqueta con atributo=valor
* `//etiqueta[@atributo='valor']` → Elemento con atributo específico
* `//etiqueta[text()='Texto exacto']` → Elemento cuyo texto interno sea ese
* `//etiqueta[contains(text(),'Texto parcial')]` → Elemento cuyo texto contenga esa frase
* `//etiqueta[@attr1='v1' and @attr2='v2']` → Combinar condiciones
* `//etiqueta[position()=2]` → Segundo elemento de ese tipo
* `*` → Cualquier etiqueta

### ✅ Ejemplos prácticos:

```xpath
//button[@id='submit']
//input[@type='text']
//div[text()='Text box']
//span[contains(text(),'Links')]
//*[@id='userName' or @type='text']
//ul/li[3]                  # Tercer item dentro de una lista
//div[@class='card'][2]     # Segundo div con clase 'card'
```

### 🧠 Consejo: ¿CSS o XPath?

* Usá **CSS** cuando sea simple: por clase, id, o atributos comunes.
* Usá **XPath** cuando necesitás lógica más compleja (texto, posiciones, múltiples condiciones).

---

### 🚀 Cómo usarlos en Selenium

```python
from selenium.webdriver.common.by import By

# CSS
driver.find_element(By.CSS_SELECTOR, "input#userName")

# XPath
driver.find_element(By.XPATH, "//input[@id='userName']")
```

---

### 🧪 Ejercicio mental:

> Querés hacer click en el segundo botón de una página con 3 botones iguales, ¿cómo lo hacés?

```python
# Con XPath usando posición
boton2 = driver.find_element(By.XPATH, "(//button)[2]")
boton2.click()
```

---