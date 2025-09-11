#input

print("Cual es tu nombre?")

nom=input()

print("Cual es tu apellido?")
ap=input()

print("Dame el valor de A")
a=int(input())
print("Dame el valor de B")
b=int(input())

suma=int(a)+int(b)
print("Tu nombre es: {} {}".format(nom,ap))
print("La suma de {} y {} es {}".format(a,b,suma))
