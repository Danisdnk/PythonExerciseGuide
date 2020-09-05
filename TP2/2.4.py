# Eliminar de una lista de palabras las palabras que se encuentren en una segunda
# lista. Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.

def crearcopialista(n):
    copia = []
    for i in range(len(n)):
        copia.append(n[i])  # el for arranca
    return copia


def listaresultante(original, eliminar):
    resultado = crearcopialista(original)
    for i in range(len(original)):
        if original[i] in eliminar:
            resultado.remove(original[i])
    return resultado


original = ["一", "二", "三", "四", "午", "六"]  # lista la original #son numeros hasta el 6
eliminar = ["四", "午", "六"]  # lista a eliminar
resultado = listaresultante(original, eliminar)
print("original:", original)
print("a eliminar:", eliminar)
print("lista resultante:", resultado)
