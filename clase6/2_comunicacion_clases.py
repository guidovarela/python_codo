""" 
    Comunicacion entre clases
        Clases: Cliente-Banco
"""

#Definicion de las clases

class Cliente:
    def __init__(self, nombre, apellido, nroCliente):
        # Metodo constructor para enviar atributos de clase
        self.nombre = nombre
        self.apellido = apellido
        self.nroCliente = nroCliente
        self.monto = 0

    def depositar(self, monto):
        # Metodo para depositar
        self.monto += monto

    def extraer(self, monto):
        # Metodo para extraer
        self.monto -= monto

    def ver_monto(self):
        return self.monto

    def imprimir(self):
        print(f"Nro de cliente: {self.nroCliente}")
        print(f"{self.apellido}, {self.nombre}")
        print(f"Saldo: ${self.monto}")

class Banco:

    def __init__(self):
        self.cliente1 = Cliente("Guido","Varela",1001)
        self.cliente2 = Cliente("Marcela","Morello",1002)
        self.cliente3 = Cliente("Diego", "Armando",1003)
        

    def operar(self):
        self.cliente1.depositar(10000)
        self.cliente2.depositar(34000)
        self.cliente3.depositar(23556)
        self.cliente2.extraer(3790)
        self.cliente1.extraer(7888)
    
    def depositos_totales(self):
        fondos = self.cliente1.monto + self.cliente2.monto + self.cliente3.monto
        print(f"Fondos totales del Banco: ${fondos}")

        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()

# Programa Principal
nuevoBanco = Banco()
nuevoBanco.operar()
nuevoBanco.depositos_totales()
