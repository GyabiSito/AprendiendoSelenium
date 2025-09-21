## 🧪 Selenium: Configuración y uso básico con Chrome o Firefox

### 📦 Instalación de dependencias

Primero, instalamos Selenium:

```bash
pip install selenium
```

---

### 🧰 Descarga de drivers (según el navegador)

* **Chrome** → [https://googlechromelabs.github.io/chrome-for-testing/#stable](https://googlechromelabs.github.io/chrome-for-testing/#stable)
* **Firefox (GeckoDriver)** → [https://geckodriver.org/](https://geckodriver.org/)

Guardá el driver descargado en una carpeta local, por ejemplo:

```text
C:\Drivers\chromedriver-win64\chromedriver.exe
```

---

### 🧪 Código de ejemplo con Selenium (Chrome o Firefox)

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.keys import Keys

# Cambiá esto por el path a tu driver
chrome_driver_path = r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe"
firefox_driver_path = r"C:\\Drivers\\geckodriver.exe"  # si usás Firefox

# ---------- OPCIÓN 1: Chrome ----------
chrome_service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service)

# ---------- OPCIÓN 2: Firefox ----------
# firefox_service = FirefoxService(executable_path=firefox_driver_path)
# driver = webdriver.Firefox(service=firefox_service)

# Navegamos a una URL
driver.get("https://demoqa.com/text-box")

# Mostramos el título de la página
print(driver.title)

# Cerramos el navegador
driver.close()
```

---

### 📝 Notas

* Podés usar `driver.quit()` en lugar de `driver.close()` si querés cerrar todo el navegador y no solo la pestaña activa.
* Asegurate que la versión del driver coincida con la del navegador que tenés instalado.

---
