## Generación de Reportes en Pytest

Este proyecto utiliza dos opciones para generar reportes automáticos de tests:

1. [`pytest-html`](https://github.com/pytest-dev/pytest-html) — genera un reporte HTML simple.
2. [`Allure`](https://docs.qameta.io/allure/) — genera reportes interactivos y visualmente más completos.

---

## ✅ Requisitos previos

* Python 3.7+
* Pip
* Pytest instalado (`pip install pytest`)
* Tener agregado el ejecutable de Allure en tu `PATH` (explicado más abajo)

---

## 1. Reporte HTML con `pytest-html`

### 🛠️ Instalación

```bash
pip install pytest-html
```

### ▶️ Ejecución

```bash
pytest .\Fixture.py --html=ReporteFixture.html
```

Esto genera un archivo `ReporteFixture.html` en el mismo directorio.

---

## 2. Reportes con Allure (más visuales e interactivos)

### 🛠️ Instalación

```bash
pip install allure-pytest
```

### 📦 Instalación del binario de Allure (Commandline)

1. Descargá la versión de Allure desde Maven:
   [Allure Commandline 2.13.9 (ZIP)](https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.9/allure-commandline-2.13.9.zip)

2. Descomprimí el `.zip` en alguna carpeta, por ejemplo:
   `C:\Tools\Allure\`

3. Agregá la ruta a la carpeta `/bin` al `PATH` de tu sistema.
   Ejemplo:
   `C:\Tools\Allure\bin`

4. Verificá que funcione:

```bash
allure --version
```

---

### ▶️ Ejecución

#### Paso 1: Ejecutar los tests con Allure activado

```bash
pytest .\Fixture.py --alluredir=allure-results
```

Esto guarda los resultados "crudos" en la carpeta `allure-results`.

#### Paso 2: Generar el reporte

```bash
allure generate allure-results --clean -o allure-report
```

Esto genera un reporte estático en la carpeta `allure-report`.

#### Paso 3 (opcional): Servir el reporte en localhost

```bash
allure serve allure-results
```

Esto levanta un servidor local y abre el reporte en el navegador. Ideal para ver el resultado rápido y visualmente.

---

## 📁 Estructura esperada

```
/tests
  Fixture.py
  ...
/allure-results        <-- Se genera automáticamente
/allure-report         <-- Se genera con allure generate
ReporteFixture.html    <-- Si usás pytest-html
```

---

## 📌 Notas

* `--clean` elimina el contenido anterior del reporte antes de generar uno nuevo.
* Si necesitás cambiar el puerto o host del `allure serve`, podés usar `--port` y `--host`.

```bash
allure serve allure-results --port 8080
```

---
