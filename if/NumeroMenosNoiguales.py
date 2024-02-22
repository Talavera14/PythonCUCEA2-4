#Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor.
#No Considerar el caso en que ambos números son iguales.
print('Cual de los siguientes números es menor?')
numero1 = int(input("Ingresa primer número:"))
numero2 = int(input("Ingresa segundo número:"))
if numero1 < numero2:
    print("primer número es menor que el segundo número")
elif numero2 < numero1:
    print("segundo número es menor que el primer número")