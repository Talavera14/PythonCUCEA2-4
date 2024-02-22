# Escriba un programa que pida tres números y que escriba si son los tres iguales,
# si hay dos iguales o si son los tres distintos.
print("Ingresa 3 números y date cuenta si son iguales o diferentes")
numero1 = int(input('Ingresa Num 1:'))
numero2 = int(input('Ingresa Num 2:'))
numero3 = int(input('Ingresa Num 3:'))
if (numero1 == numero2 and numero2 == numero3):
    print("Todos los números son iguales")
elif (numero1 == numero2):
    print("Dos números son iguales")
elif(numero1 == numero3):
    print("Dos números son iguales")
elif(numero2 == numero3):
    print("Dos números son iguales")
else:
    print("Todos los números son distintos")