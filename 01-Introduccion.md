## 🐍 Aprendiendo Python para Selenium

Este es un mini repaso de Python pensado para automatizar con Selenium. Vamos desde variables hasta estructuras de control, funciones e input de usuario. Dale que va.

---

### 🔸 Variables

```python
a = 10
b = 20.5

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b

print("la suma es " + str(suma))
print("la resta es " + str(resta))
print("la multiplicacion es " + str(multiplicacion))
print("la division es " + str(division))

nombre = "Jose"
ap = "Hernandez"
print(nombre + " " + ap)

print(type(a))
print(type(b))
print(type(suma))
print(type(resta))
print(type(multiplicacion))
print(type(division))
```

---

### 🔄 Conversiones

```python
a = 20
b = 20
nombre = "jose"

print(type(a))
print(type(nombre))
print("La suma es: " + str(a + b))

a = str(a)
b = float(b)
b2 = str(b)

print(type(a))
print(type(b))
print("La suma de String es " + a + b2)
```

---

### 🧵 Cadenas de texto

```python
texto = "Hola bienvenido a python"
print(texto)
print(texto[3])
print(texto[5:15])
print(texto[-6:])

nombre = "juan"
print(nombre.upper())
print(nombre.lower())
print(nombre.capitalize())

cadena = "php,java,selenium,javascript"
print(cadena)
print(cadena.split(","))

nom = "Juan"
ap = "Perez"
print("Tu nombre es: {} y tu apellido es: {}".format(nom, ap))
print(f"Tu nombre es: {nom} y tu apellido es: {ap}")
```

---

### 🧠 Condicionales

```python
a = 20
b = 10
c = 1

if a > b:
    print("a es mayor que b")
else:
    print("b es mayor que a")

nom = "juan"
if nom == "juan":
    print("Es juan")
else:
    print("No es juan")

if a < b:
    print("a es menor o igual que b")
elif a == b:
    print("a es igual que b")
else:
    print("a es mayor que b")

# Comentario de una línea
# Comentario estilo bloque
'''
if a < b or a > c:
    print("a es menor que b o mayor que c")
else:
    print("a no es menor que b o mayor que c")
'''
```

---

### ⚙️ Funciones

```python
def saludo():
    print("Hola a todos")

saludo()

def saludo_nombre(nombre):
    print("Hola " + nombre)
    return nombre

saludo_nombre("Jose")

def suma(a, b):
    return a + b

print(suma(1, 2))

def suma_resta(a, b):
    return a + b, a - b

def suma2(*args):
    res = 0
    for n in args:
        res += n
    return res

print(suma2(1, 2, 3, 4))
print(suma2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
```

---

### ⌨️ Introducir valores

```python
print("Cual es tu nombre?")
nom = input()

print("Cual es tu apellido?")
ap = input()

print("Dame el valor de A")
a = int(input())
print("Dame el valor de B")
b = int(input())

suma = a + b
print("Tu nombre es: {} {}".format(nom, ap))
print("La suma de {} y {} es {}".format(a, b, suma))
```

---

### 📚 Listas

```python
lenguajes = ["php", "java", "python"]
print("lenguaje seleccionado: " + lenguajes[0])
print(lenguajes)

lenguajes.append("javascript")
print(lenguajes)

lenguajes.remove("php")
print(lenguajes)

lenguajes.pop()
print(lenguajes)

lenguajes.insert(1, "ruby")
print(lenguajes)

lenguajes.sort()
print(lenguajes)

lenguajes.reverse()
print(lenguajes)

print("El largo de la lista es: " + str(len(lenguajes)))
print(lenguajes[1:3])
```

---

### 🔁 Loops

```python
for x in range(10):
    if x == 3:
        continue
    if x == 5:
        break
    print(x)

print("------------------------")

for x in range(5, 10, 2):
    print(x)

print("------------------------")

colores = ["rojo", "verde", "azul"]
for color in colores:
    print(color)

print("------------------------")

nombre_completo = "jose hernandez"
for letra in nombre_completo:
    print(letra)

print("------------------------")

inicio = 1
fin = 10
while inicio <= fin:
    print(inicio)
    inicio += 1
    if inicio == 5:
        continue
    if inicio == 7:
        break
```

---

### ⚖️ Comparaciones

```python
a = 10
b = 5
c = 50

print("Son iguales: " + str(a == b))
print("Son diferentes: " + str(a != b))
print("Es mayor: " + str(a > b))
print("Es menor: " + str(a < b))
print("Es mayor o igual: " + str(a >= b))
print("Es menor o igual: " + str(a <= b))

print("a > b y a < c: " + str(a > b and a < c))
print("a > b o a < c: " + str(a > b or a < c))
```