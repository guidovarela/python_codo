""" Operadores de pertenencia
    not in, in
    Devuelve True o False por consola
 """

 #Muestra en consola si existe o no una letra

#texto = input("Ingresar el texto para evaluar: ")

sabores = "frutilla, vainilla, chocolate"

print("frutilla" in sabores) #True
print("Frambuesa" in sabores) #False

print("Chocolate" not in sabores)
print("Dulce de leche" not in sabores)

buscar_Sabores = str(input("Insertar el sabor buscado: "))
print(buscar_Sabores in sabores) 
