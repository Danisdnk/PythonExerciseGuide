import  random

# a Cargar una lista con números al azar de cuatro dígitos.
# La cantidad de elementos también será un número al azar de dos dígitos.


def tamañolista(elementos):
    lista=[]
    for i in range(elementos):
        lista.append(random.randint(0, 99))
    print(lista)
    return lista

def eliminarvalorlista(lista):
    n = int(input("elija que valor de la lista quiere eliminar :"))
    lista.remove(n)
    print(lista)

lista = random.randint(1 ,5)
resultadolista=tamañolista(lista)
print(sum(resultadolista))  # B

eliminarvalorlista(resultadolista)  # C
