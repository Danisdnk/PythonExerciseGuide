'''1. Desarrollar una función que reciba tres números positivos y devuelva el mayor de
los tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor estricto devolver -1. No utilizar operadores lógicos (and, or, not).
Desarrollar también un programa para ingresar los tres valores, invocar a la función y mostrar el
máximo hallado, o un mensaje informativo si éste no existe.'''


def calcularMayor(a, b, c):
    if a < b:
        calcularMayor(b, a, c)
    elif a > c:
        return print(a, "es el valor maximo")
    elif c > a:
        return print(c, "es el valor maximo")
    else:
        return print("no hay valor maximo")


v1 = int(input("Ingrese un numero entero:"))
v2 = int(input("Ingrese un numero entero 2:"))
v3 = int(input("Ingrese un numero entero 2:"))

calcularMayor(v1, v2, v3)