def rellenarmatriz(matriz):
    #autodetectamos el tamaño de la matriz
    g = [[1, 2, 3, 4],[ 12, 13, 14, 5,], [11, 16, 15, 6],[ 10, 9, 8, 7]]  # <-------------- "
    filas=len(matriz)
    col=len(matriz[0])
    for f in range(filas):
        for c in range(col):
            matriz[f][c] = g[f][c] #guarda valor en posicion de mtriz

def imprimirmatriz(matriz):
    filas=len(matriz)
    col=len(matriz[0])
    for f in range(filas):
        for c in range (col):
            print("%3d" % matriz[f][c],end="")
        print()

filas = int(input("ingrese cantidad de filas"))

columnas = filas
matriz = []
for f in range(filas):
    matriz.append([0]*columnas)

rellenarmatriz(matriz)
imprimirmatriz(matriz)