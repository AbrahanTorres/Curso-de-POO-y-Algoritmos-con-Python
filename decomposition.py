#This example is to modeling a car using the decomposition model.

class Automovil:  
    def __init__(self, modelo, marca, color):  #Constructor init
        self.modelo = modelo  #inicializamos las variables de instancias
        self.marca = marca
        self.color = color
        self._estado = "en_reposo"   #Usamos una variable privada con el _ al principio. Damos un estado, comienza en reposo.
        self.motor = Motor(cilindros=4)
    
    def acelerar(self, tipo="despacio"):
        if tipo == "rapida":
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
        
        self._estado = "en_movimiento"

class Motor:
    def __init__(self, cilindros, tipo="gasolina"):  # tipo="gasolina" este es un parámetro por defecto o default keyword.
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0
    
    def inyecta_gasolina(self, cantidad):
        pass