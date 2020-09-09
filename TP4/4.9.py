
#9. Desarrollar una función que devuelva una subcadena con los últimos N caracteres
#de una cadena dada. La cadena y el valor de N se pasan como parámetros.

def cortacadena(n,cadena):
    largo = len(cadena)-n
    subcadena = cadena[largo:]
    return cadena, subcadena

cadena = input("Ingrese la cadena que quiere cortar")
n = int(input("cuantos caracteres de la cadena va a mostrar"))

original, sub = cortacadena(n, cadena)
print(original, "-cadena original-")
print(sub, "-cadena resultante del corte-")

#La arrogancia atrae el odio y la envidia.
#La elegancia despierta el respeto y el amor
