print("Hola buenos dias")
precio = float(input("Ingresar precio:"))
cantidad = int(input("Ingresar cantidad de manzanas:"))
Totalpagar = precio * cantidad
print(f"Total a pagar: {Totalpagar}")
while cantidad !=0:
    cantidad = float(input("ingresa cantidad de manzanas: "))
    if cantidad ==0:
        break
if cantidad == 18 :
    descuento = (cantidad * precio) *.15
    print(f"el descuento es de {descuento}")
elif cantidad >= 10 :
    descuento = (cantidad * precio) *.10
    print(f"el descuento es de {descuento}")
else:
    print("gracias por comprar")
totalAPagar = (cantidad * precio) - descuento

print(f"Total a pagar {totalAPagar} " )