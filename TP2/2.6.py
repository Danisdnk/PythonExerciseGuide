#Escribir una función que reciba una lista de números enteros como parámetro y la
#normalice, es decir que todos sus elementos deben sumar 1.0,
#respetando las proporciones relativas que cada elemento tiene en la lista original.
#Desarrollar también un programa que permita verificar el comportamiento de la función.
#Por ejemplo, normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50]


def normalizarlista(enteros):
    total = sum(enteros)
    normalizado = []
    for i in range(len(enteros)):
        porcentaje = enteros[i] / total
        normalizado.append(porcentaje)
        # print("entero: %d normalizar %.2f"%( enteros[i], porcentaje), end=", ")
    return normalizado


listaenteros = [1, 1, 2]
res = normalizarlista(listaenteros)
print("lista original:", listaenteros, "Lista normalizada: ", end="")
for i in range(len(res)):
    print("%.2f" % (res[i]), end=" ")  #print(f"{res[i]:.2f}", end=" ")