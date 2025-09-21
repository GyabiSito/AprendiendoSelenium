# 📑 Manejo de Excel con openpyxl en pruebas automatizadas

Este módulo implementa una clase `Funexcel` que facilita la lectura y escritura de datos en archivos Excel, con soporte de la librería [openpyxl](https://openpyxl.readthedocs.io/en/stable/).

Se utiliza principalmente para **Data Driven Testing (DDT)** en pruebas automatizadas, permitiendo usar hojas de Excel como fuente de datos.

---

## ⚙️ Clase `Funexcel`

### Inicialización

```python
class Funexcel:
    def __init__(self, driver=None):
        self.driver = driver
```

El parámetro `driver` es opcional y se mantiene por compatibilidad con pruebas que integran Selenium.

---

### Métodos principales

#### 1. Contar filas

```python
def getRowCount(self, file, sheetName):
    """Devuelve el número de filas usadas en una hoja"""
```

* **Parámetros:** ruta del archivo, nombre de la hoja.
* **Retorna:** número total de filas con datos.

#### 2. Contar columnas

```python
def getColumnCount(self, file, sheetName):
    """Devuelve el número de columnas usadas en una hoja"""
```

* **Parámetros:** ruta del archivo, nombre de la hoja.
* **Retorna:** número total de columnas con datos.

#### 3. Leer datos

```python
def readData(self, file, sheetName, rownum, colnum):
    """Lee el valor de una celda"""
```

* **Parámetros:** archivo, hoja, número de fila y número de columna.
* **Retorna:** valor almacenado en la celda.

#### 4. Escribir datos

```python
def writeData(self, file, sheetName, rownum, colnum, data):
    """Escribe un valor en una celda"""
```

* **Parámetros:** archivo, hoja, fila, columna, valor a escribir.
* Guarda automáticamente el archivo tras la escritura.

---

## ▶️ Ejemplo de uso

```python
from funciones.Funciones_Excel import Funexcel

# Crear instancia
fe = Funexcel()

# Ruta al Excel
ruta = "./datos.xlsx"

# Obtener filas y columnas
filas = fe.getRowCount(ruta, "Hoja 1")
columnas = fe.getColumnCount(ruta, "Hoja 1")

print(f"Filas: {filas}, Columnas: {columnas}")

# Leer datos de la celda (fila 2, col 1)
nombre = fe.readData(ruta, "Hoja 1", 2, 1)
print("Nombre:", nombre)

# Escribir resultados en la hoja
fe.writeData(ruta, "Hoja 1", 2, 5, "OK")
```

---

## 📌 Notas importantes

* Se requiere instalar **openpyxl**:

  ```bash
  pip install openpyxl
  ```
* Es recomendable manejar rutas absolutas o relativas con `pathlib`.
* Esta clase puede integrarse con pruebas `unittest` o `pytest` para leer datos dinámicamente desde Excel.
