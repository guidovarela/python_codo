""" 
    Encapsulamiento
    Atributos y metodos protegidos

    Clase: Vehiculo
        marca, modelo, color, dominio

    los atrubutos encapsulados (no accesible) comienzan con __
"""

class Vehiculo:

    def __init__(self, id, marca, modelo, color, dominio):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.__dominio = dominio

    def info_vehiculo(self):
        print(f"Vehiculo nro {self.id}")
        print(f"Datos: {self.marca} {self.modelo} {self.color}")
        print(f"Patente: {self.__dominio}")

auto1 = Vehiculo(1001,"Ford","Mondeo","Gris plata","ad-3456-aa🚗")
auto1.info_vehiculo()
