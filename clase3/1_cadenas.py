""" 
cadena = "Hola Mundo"
es un array de caracteres
 """

cadena = "Hola Mundo 123 Polo"

print("Primer letra", cadena[0])

#cantiada de caracteres, longitud de una cadena -> length -> len(objeto)
print(len(cadena))

#Buscar dentro de una cadena
print(cadena.find("Mundo"))

#iterar una cadena

for valor in cadena:
    if valor.isnumeric():
        print("*"*10)
        print(valor)

# Reemplazar un texto, usando replace("old_Data","new_Data")
print("Antes: ", cadena)
cadena = cadena.replace("Hola","Adios")
print("Despues: ", cadena)


# Upper() -> string a mayusculas
# Lower() -> string a minusculas
# strip() -> Elimina los espacios al principio y al final. Elimina caracteres indicado entre ()

cadena2 = "Adios mundo cruel"
print(cadena2.strip())


