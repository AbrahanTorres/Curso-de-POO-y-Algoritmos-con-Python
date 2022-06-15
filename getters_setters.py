class CasillaDeVotacion:
    def __init__(self, identificador, pais):
        self.__identificador = identificador
        self.__pais = pais
        self.__region = None

    @property    #This one is getter because there are nothing describing it, it is the first.
    def region(self):
        return self.__region
    
    @region.setter #For the second one it is necessary to use the word setter after the property name.
    def region(self, region):
        if region in self.__pais:
            self.__region = region
        else:
            raise ValueError(f"La región {region} no es valida en {self.__pais}")

casilla = CasillaDeVotacion(123, ["Madrid", "Barcelona", "Sevilla", "Malaga", "Canarias", "Cantabria"])
print(casilla.region)
casilla.region = "Barcelona"
#casilla.region = input(str("Ingrese su ciudad de votación: "))
print(casilla.region)
