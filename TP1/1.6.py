# 6. Desarrollar una función que reciba como parámetros dos números enteros positivos
# y devuelva el número que resulte de concatenar ambos valores. Por ejemplo,
# si recibe 1234 y 567 debe devolver 1234567. No se permite utilizar facilidades de
# Python no vistas en clase.


def concatenar(x, y):
    # devolver=print(x,y,end='')
    print(y, end='')
    print(x, end='')


b = int(input("Ingrese un numero entero:"))
a = int(input("Ingrese un numero entero 2:"))
concatenar(a, b)
