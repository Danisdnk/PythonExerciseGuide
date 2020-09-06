# Escribir una función que reciba una lista como parámetro y devuelva True si la lista
# está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
# ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar
# además un programa para verificar el comportamiento de la función.

def crearcopialista(n):  # creo copia de la lista con otra referencia
    copia = []
    for i in range(len(n)):
        copia.append(n[i])
    return copia


def comprobarordenlista(listaA, listaB):
    for i in range(len(listaA)):
        if listaA[i] in listaB:
            if listaA[i] > listaB[i]:
                print("listaA", listaA)
                ret = True
            else:
                ret = False
    return ret


def emitirmensaje(val):
    if val:
        print("la lista  esta ordenada ascendentemente")
    else:
        print("la lista no esta ordenada ascendentemente")

listaA = ["Abril", "Eleonor", "Alejo"] # con caracteres
#listaA = [1, 3, 2,5,"Abril", "Eleonor", "Alejo"] # con numeros
listaB = crearcopialista(listaA)
listaB.sort()  # lista ascendente
comp = comprobarordenlista(listaA, listaB)
print(listaA, "Lista original sin ordenar")
print(listaB, "Lista ordenanada ascendente A-Z ,1-100")

emitirmensaje(comp)


