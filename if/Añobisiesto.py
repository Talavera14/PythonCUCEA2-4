#Hacer un programa que permita saber si un año es bisiesto.
#Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100,
#excepto que también sea divisible por 400
print("Detector de años bisiestos")
Año = int(input("Ingresar año a analizar:"))
if (Año % 4 == 0 and (not Año % 100 == 0)):
    print("SI es año bisiesto")
elif (Año % 400 == 0):
    print("SI es año bisiesto")
else:
    print("NO es año bisiesto")