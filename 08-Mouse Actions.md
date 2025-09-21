# 🖱️ Mouse Actions en Selenium

En Selenium, además de los clicks simples, podemos automatizar una variedad de **acciones con el mouse** gracias a la clase `ActionChains`. Esto incluye interacciones comunes como *hover*, *doble click*, *click derecho*, *drag & drop*, clicks en coordenadas específicas y hasta simular atajos como copiar y pegar.

En este documento te muestro cada tipo de acción, el HTML de ejemplo y el test en Python. La idea es que tengas un mini-laboratorio de prácticas para dominar estas interacciones.

---

## 1️⃣ Hover (pasar el mouse por encima)

**Caso de uso:** Menús desplegables que aparecen sólo cuando pasás el mouse.

### HTML (`01-Sublists.html`)

```html
<ul class="menu">
  <li>
    <a href="#" id="menu_admin_viewAdminModule">Admin</a>
    <ul>
      <li>
        <a href="#" id="menu_admin_viewUserManagment">User Management</a>
        <ul>
          <li>
            <a href="#" id="menu_admin_viewSystemUsers">System Users</a>
          </li>
        </ul>
      </li>
    </ul>
  </li>
</ul>
```

### Test en Python

```python
actions.move_to_element(admin).perform()
WebDriverWait(driver, 5).until(EC.visibility_of(user_mgmt))

actions.move_to_element(user_mgmt).perform()
WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "menu_admin_viewSystemUsers")))

system_users = driver.find_element(By.ID, "menu_admin_viewSystemUsers")
actions.move_to_element(system_users).click().perform()
```

👉 Paso a paso: primero hover en **Admin**, después en **User Management**, y finalmente clic en **System Users**.

---

## 2️⃣ Double Click (doble click)

**Caso de uso:** Activar acciones especiales (ejemplo: abrir un archivo, editar un campo).

### HTML (`02-DobleClick.html`)

```html
<div id="box">Doble click acá 👆</div>
```

```javascript
box.addEventListener("dblclick", () => {
  box.textContent = "¡Doble click detectado! ✅";
});
```

### Test en Python

```python
box = driver.find_element(By.ID, "box")
actions.double_click(box).perform()

WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.ID, "box"), "¡Doble click detectado!")
)
```

👉 Con `actions.double_click()` simulamos el doble click real.

---

## 3️⃣ Right Click (click derecho / context menu)

**Caso de uso:** Menús contextuales o acciones alternativas al click izquierdo.

### HTML (`03-ClickDerecho.html`)

```html
<div id="target">Click derecho acá 🖱️</div>
```

```javascript
target.addEventListener("contextmenu", (e) => {
  e.preventDefault();
  target.textContent = "¡Click derecho detectado! 🎯";
});
```

### Test en Python

```python
target = driver.find_element(By.ID, "target")
actions.context_click(target).perform()

WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.ID, "target"), "¡Click derecho detectado!")
)
```

👉 Usamos `actions.context_click()` para el menú contextual.

---

## 4️⃣ Drag and Drop (arrastrar y soltar)

**Caso de uso:** Mover elementos de un lado a otro, tipo Trello o subir archivos.

### HTML (`04-DragAndDrop.html`)

```html
<div id="drag" draggable="true">Arrástrame</div>
<div id="dropzone">Suelta aquí</div>
```

```javascript
dropzone.addEventListener("drop", (e) => {
  e.preventDefault();
  dropzone.textContent = "¡Elemento soltado! 🎯";
});
```

### Test en Python

```python
source = driver.find_element(By.ID, "drag")
target = driver.find_element(By.ID, "dropzone")

actions.drag_and_drop(source, target).perform()

WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.ID, "dropzone"), "¡Elemento soltado!")
)
```

👉 `drag_and_drop()` hace todo: click, arrastrar y soltar en destino.

---

## 5️⃣ Click en coordenadas específicas (X/Y)

**Caso de uso:** Interacciones en un canvas, mapas o gráficos.

### HTML (`05-ClickXYTest.html`)

```html
<div id="canvas"></div>
```

```javascript
canvas.addEventListener("click", (e) => {
  const x = e.clientX - rect.left;
  const y = e.clientY - rect.top;
  // se dibuja un puntito rojo
});
```

### Test en Python

```python
canvas = driver.find_element(By.ID, "canvas")

actions.move_to_element_with_offset(canvas, 50, 80).click().perform()
actions.move_to_element_with_offset(canvas, 150, 120).click().perform()

dots = canvas.find_elements(By.CLASS_NAME, "dot")
self.assertGreaterEqual(len(dots), 2)
```

👉 Usamos `move_to_element_with_offset` para clicks relativos al elemento.

---

## 6️⃣ Copiar y pegar (Ctrl+C / Ctrl+V)

**Caso de uso:** Validar atajos de teclado sobre inputs.

### HTML (`06-CopiarPegar.html`)

```html
<input type="text" id="source" value="Texto para copiar">
<input type="text" id="target" placeholder="Pegá aquí con Ctrl+V">
```

### Test en Python

```python
source = driver.find_element(By.ID, "source")
target = driver.find_element(By.ID, "target")

source.send_keys(Keys.CONTROL, "a")
source.send_keys(Keys.CONTROL, "c")

target.click()
target.send_keys(Keys.CONTROL, "v")

self.assertEqual(source.get_attribute("value"), target.get_attribute("value"))
```

👉 Selenium simula `Ctrl+A`, `Ctrl+C` y `Ctrl+V` sobre los inputs.

---

# 🎯 Conclusión

Con `ActionChains` podés simular casi cualquier interacción del mouse:

* Hover para menús ocultos.
* Doble click para abrir/editar.
* Click derecho para menús contextuales.
* Drag & Drop para mover elementos.
* Clicks en coordenadas específicas.
* Y combinarlos con atajos de teclado como copiar/pegar.

