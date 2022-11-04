""" 
Operadores compuestos

Suma:           +=
Resta:          -=
Division        /=
Division Entera //=
Modulo (resto)  %=
Multi           *=
potencia        **=
 """


#Entrada de numeros
num1 = int(input("Ingresar el 1er numero"))
num2 = int(input("Ingresar el 2do numero"))

#mostrar los datos ingresados
print(f"Los datos ingresados son: {num1} y {num2}")

#realizar operacion compuesta
num1 += num2

print(num1)
print(num2)