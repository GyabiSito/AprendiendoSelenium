def saludo():
    print("Hola a todos")


saludo()


def saludo_nombre(nombre):
    print("Hola " + nombre)
    return nombre


saludo_nombre("Jose")


def suma(a, b):
    return a + b


suma(1, 2)


def suma_resta(a, b):
    return a + b, a - b


def suma2(*args):
    res = 0
    for n in args:
        res += n
    return res

print(suma2(1, 2, 3, 4))
print(suma2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))