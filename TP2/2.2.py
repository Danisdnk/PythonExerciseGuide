#2. Escribir funciones para:
# a. Generar una lista de 50 números aleatorios del 1 al 100.
# b. Recibir una lista como parámetro y devolver True si la misma contiene algún
# elemento repetido. La función no debe modificar la lista.
# c. Recibir una lista como parámetro y devolver una nueva lista con los elementos
# únicos de la lista original, sin importar el orden.
# Combinar estas tres funciones en un mismo programa


import random


def crearlista(elementos):
    lista = []
    for i in range(elementos):
        lista.append(random.randint(0, 100))
    return lista


def repeticionvalorlista(lista):
    """Chequea si una lista tiene elementos repetidos"""
    rep = False
    for i in range(len(lista)):
        if lista.count(lista[i]) >= 1:
            rep = True
            break
    return rep


def borrarrepetidos(lista):
    """Toma una lista y devuelve otra con los elementos únicos"""
    nuevalista = []
    for i in range(len(lista)):
        if lista.count(lista[i]) == 1:
            nuevalista.append(lista[i])
    return nuevalista

elementos = random.randint(1, 50)
resultadolista = crearlista(elementos)
print("lista original: ", resultadolista, len(resultadolista))
rep = repeticionvalorlista(resultadolista)

if rep:
    unicos = borrarrepetidos(resultadolista)
    print("hay elementos repetidos",end=",")
    if len(unicos) > 0:
        print("los elementos unicos en la lista son: ", unicos)
    else:
        print("no habia elementos unicos en la lista")
else:
    print("no hay elementos repetidos")
    print("lista original: ", resultadolista)
