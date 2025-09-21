# 🐍 Guía Rápida: Entornos Virtuales en Python + pytest paralelo

## 🎯 ¿Qué es un entorno virtual?

Un entorno virtual te permite crear un **espacio aislado** para instalar paquetes de Python **sin afectar el sistema global**.

Ideal para evitar conflictos de dependencias entre proyectos.

---

## 🧱 Opciones para crear entornos virtuales

### 1. Con `venv` (incluido en Python 3.3+)

```bash
python -m venv .venv
```

Crea una carpeta `.venv` con:

* su propio Python
* su propio pip

### 2. Con `virtualenv` (librería externa)

```bash
pip install virtualenv
virtualenv MV1
```

Hace lo mismo, pero ofrece más compatibilidad y opciones avanzadas.

> 💡 Si usás Python moderno (3.10+), `venv` es más que suficiente.

---

## ⚙️ Activar un entorno virtual

### En PowerShell

```bash
.\.venv\Scripts\Activate
```

o si usaste `virtualenv`:

```bash
.\MV1\Scripts\Activate
```

> Verás que el prompt cambia a `(.venv)` o `(MV1)` según el entorno activo.

---

## 🧼 ¿Cómo eliminar un entorno virtual?

1. Desactivá el entorno si está activo:

```bash
deactivate
```

2. Eliminá la carpeta (desde consola):

```bash
rmdir /s /q .venv
rmdir /s /q MV1
```

O desde el Explorador con clic derecho > Eliminar.

---

## 🔢 Ver la versión de Python activa

Con el entorno activado:

```bash
python -V       # versión simple
python -VV      # versión + info detallada
where python    # ubicación del binario activo
```

---

## ⚖️ Ejecutar tests en paralelo con pytest

Si querés correr tus tests usando varios procesos:

### Instalá pytest y pytest-xdist

```bash
pip install pytest pytest-xdist
```

### Ejecutá con `-n`

```bash
pytest -n 5   # Corre 5 instancias de test en paralelo
```

Ideal para acelerar tests pesados o suites grandes.

---

## 🔄 Recomendación

* Usá **1 entorno virtual por proyecto**
* No anides entornos (por ejemplo, .venv y MV1 en el mismo lugar)
* Si usás Python moderno, preferí `venv` antes que `virtualenv`

---