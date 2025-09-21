# 📌 README: Assertions en Python con Pytest

## ✨ Propósito de las Assertions

Las **assertions** (aserciones) son fundamentales para validar que el comportamiento de nuestro sistema es el esperado. En el contexto de pruebas automatizadas con **pytest**, nos permiten:

* Validar condiciones lógicas.
* Generar errores si una condición falla.
* Obtener informes de ejecución claros y detallados.

> Sin assertions, no hay validación real en los tests. Solo estás imprimiendo cosas en consola.

---

## 🔹 Sintaxis básica

```python
assert condicion, "Mensaje opcional de error"
```

Ejemplo:

```python
assert 2 + 2 == 4, "La suma está mal"
```

---

## 🔹 Ejemplos típicos

### Comparaciones numéricas

```python
assert a == b
assert a != b
assert a > b
assert a < b
```

### Strings

```python
assert "abc" in "abcdef"
assert texto.startswith("Hola")
```

### Colecciones

```python
assert len(lista) == 5
assert 3 in [1,2,3,4]
```

### Booleanos

```python
assert True
assert not False
```

---

## ✅ Soft Assertions con `assertpy`

A diferencia de `assert` nativo que corta la ejecución al fallar, con `assertpy` podemos seguir evaluando varias condiciones.

Ejemplo:

```python
from assertpy import assert_that, soft_assertions

with soft_assertions():
    assert_that(1).is_equal_to(2)
    assert_that("hola").contains("z")
    assert_that([1, 2, 3]).is_length(4)
```

> Todas las fallas se reportan al final. Ideal para validaciones masivas.

### Instalación:

```bash
pip install assertpy
```

---

## ❌ Errores comunes

### 1. ❌ Usar `--soft-asserts` con pytest (NO existe ese flag)

Ese flag no es parte de `pytest`. Si querés soft assertions, usá `assertpy` como se mostró arriba.

### 2. ❌ Importación incorrecta:

```python
# INCORRECTO
from soft_assert import soft_assertions

# CORRECTO
from assertpy import soft_assertions, assert_that
```

### 3. ⚠️ Marks personalizadas sin registrar:

```python
@pytest.mark.run  # ❌ Warning: mark no registrada
```

Solución:
Agregá en `pytest.ini`:

```ini
[pytest]
markers =
    run: tests de ejecución
```

---

## 🔮 Tips de uso

* Usá `assert_that()` para legibilidad.
* Evitá condiciones dentro de `if`, usá `assert` directamente.
* Combiná con `pytest.mark.parametrize` para validar múltiples datos.
* Aprovechá `pytest.raises` para tests que esperan errores.

---

## 🔗 Recursos recomendados

* [Documentación oficial de Pytest](https://docs.pytest.org/)
* [assertpy GitHub](https://github.com/assertpy/assertpy)
* Curso de testing en Python (buscalo en YouTube, seguro hay uno bueno)

---

## 👋 Conclusión

Las assertions son el ladrillo fundamental del testeo automatizado. Usalas bien, mantené tus tests claros, y no abuses de prints para validar lógica – pytest está para eso.
