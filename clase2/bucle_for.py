""" For """

#range -> genera una secuencia numerica -> array numerico -> por default, comienza en 0
""" rango = list(range(3))
print(rango) """

""" for i in range(10):
    print(i) """

""" for i in range(2,6): # [2,3,4,5]
    print(i) """
    
""" for i in range(1,5,2): # [1,3]
    print(i) """

texto = "Lucas, Morena, Lisandro, Lili, Lolo"
contador = 0

for letra in texto.lower():
    if letra == "l":
        contador += 1
print(f"Cantidad de L: {contador}")
