""" 
    Decoradores
    Permite modificar los atributos que estan encapsulados
    
 """

class Bebidas:
    def __init__(self, sabor="Uva"):
        self.__sabor = sabor

    @property
    def favorita(self):
        return (f"Mi preferida es : {self.__sabor} ")

    @favorita.setter
    def sabor_favorito(self, sabor):
        self.__sabor = sabor

bebida1 = Bebidas()
bebida1.sabor_favorito = "Naranja"

print(bebida1.sabor_favorito)

