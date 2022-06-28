import time
import sys  #python tiene un limite de recursion, importando sys se puede cambiar.
sys.setrecursionlimit(200000)  #Para amplia el límite se usa sys.setrecursionlimit(numero_limite).

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta

def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial_r(n - 1)

def main():

    n = 1000
    
    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final -comienzo)

if __name__ == "__main__":
    main()

