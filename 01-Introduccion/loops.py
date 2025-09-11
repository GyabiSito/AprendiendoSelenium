for x in range(10):
    if (x == 3):
        continue
    if (x == 5):
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

while (inicio <= fin):
    print(inicio)
    inicio += 1
    if (inicio == 5):
        continue
    if (inicio == 7):
        break



