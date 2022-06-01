#Esta clase=class puede determinar la distancia entre dos coordenadas.

class Coordenada:         #Generamos la clase llamada Coordenada.

    def __init__ (self, x, y):  #Iniciamos el método init, una coordenada tiene X y Y.
        self.x = x    #Inicializamos las variables
        self.y = y

    def distancia(self, otra_coordenada): #Generamos el método llamado distancia, "otra_coordenada" es una instancia.
        x_diff = (self.x - otra_coordenada.x)**2  #Usamos el método euclidiano para definir la diferencia de instancia.
        y_diff = (self.y - otra_coordenada.y)**2  # (Y2 - Y1) **2

        #  [(X2 - X1)**2 + (Y2 - Y1)**2]**0.5     0.5=1/2 = Raíz cuadrada. Ejemplo matemático del proceso.

        return (x_diff + y_diff)**0.5  #Retornamos la raíz cuadrada de la suma de las diferencias de distancias cada una al cuadrado. La raíz es 1/2 es decir 0.5.


if __name__ == "__main__": #Especifica que si ejecutamos el programa desde la terminal, lo podemos correr.
    coord_1 = Coordenada(3, 30)  #Generamos una instancia de la primera coordenada.
    coord_2 = Coordenada(4, 8)  #Generamos una segunda instancia de la segunda coordenada.

    print(coord_1.distancia(coord_2)) #Decimos cual es la distancia entre la coordenada  1 y le pasamos la coordenada 2.
    print(isinstance(coord_2, Coordenada)) #isinstance nos permite verificar si coordenada  2 es una instancia de coordenada.