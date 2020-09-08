#Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con
#los elementos de la primera que sean impares. El proceso deberá realizarse utilizando
#listas por comprensión. Imprimir las dos listas por pantalla.
import random


def crearlista(elementos):
    lista = []
    for i in range(elementos):
        lista.append(random.randint(0, 100))
    return lista


tamlista = random.randint(1, 10)
azar = crearlista(tamlista)
print("lista original ",azar)
listadeimpares = [azar[i]for i in range(len(azar)) if azar[i] % 2 != 0]

if len(listadeimpares)==0:
    print("no hay valores impares en la lista original")
else:
    print("lista impares ", listadeimpares)

