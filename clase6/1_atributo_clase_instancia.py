""" 
Atributo de clase y de instancia
    Clase Persona
"""

class Persona:
    # atributos de clase
    piernas = 2

    # Metodo - Constructor
    def __init__(self, nombre):
        self.nombre = nombre #atributo de instancia

user1 = Persona("Marcelo")
user2 = Persona("Benito")

print(f"{user1.nombre} tiene {user1.piernas} piernas")