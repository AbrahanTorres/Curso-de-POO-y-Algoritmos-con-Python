import random


def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista: #O(n). la función def sería O de 1, y el loop for, al tomar un dato input "lista" califica como O de n que crece lineal.
        if elemento == objetivo:
            match = True
            break
    return match

def run():
    tamano_de_lista = int(input("De que tamaño sera la lista?: "))
    objetivo = int(input("Que numero quieres encontrar?"))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

    encontrado = busqueda_lineal(lista, objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')  # Importante asignar comillas simples para diferenciarlas de las comillas dobles.


if __name__ == "__main__":
    run()