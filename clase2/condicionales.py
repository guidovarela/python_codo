num1 = 10
num2 = 1

if num1!=0 and num2!=0:
    print (num1 / num2)
""" else:
    print ("No es posible dividir por 0")
 """
# -------------------------------------------------------------------

edad = int(input("Ingresa tu edad: "))

if edad >=18:
    print(f"Podes pasar porque tenes {edad} años y sos mayor de edad")
else:
    print(f"No podes ingresar porque tenes {edad} años")


# --------------------------------------------------------------------

nota = 5

if nota >= 0 and nota < 4:
    print(f"Nota: {nota} - Desaprobado")
elif nota >=4 and nota <7:
    print(f"Nota: {nota} - Aprobado")
else:
    print(f"Nota: {nota}: Muy Bueno")

