# 3. Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
# donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos
# 10 valores de la lista.


def crearlista(n):
    lista = []
    ultimosdiez = []
    for i in range(1, n + 1):
        lista.append(i ** 2)

    if len(lista) < 10:
        print(lista)
    else:
        lista.reverse()
        for i in range(0, 9):
            ultimosdiez.append(lista[i])
        ultimosdiez.reverse()
        print(ultimosdiez)


n = int(input("ingrese la cantidad de valores para la lista"))
crearlista(n)
