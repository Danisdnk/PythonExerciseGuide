# Escribir una función que reciba como parámetro un número entero entre 0 y 3999
# y lo convierta en un número romano, devolviéndolo en una cadena de caracteres.
# ¿En qué cambiaría la función si el rango de valores fuese diferente?

# a partir de 4k no se usa mas la M para indicar la unidad de mil

def conversor(numero, unidad):
    c = numero
    val = unidad
    if c==0:
        u =" "
        return u
    if c == 1 or c == 2 or c == 3:  # hasta 300 es c
        u = val[0] * c
        return u

    elif c == 4:  # caso 4
        u = val[1]
        return u

    elif c == 9:  # caso 9
        u = val[3]
        return u
    elif 5 <= c <= 8:  # entre 5 y 8
        q = val[2]
        u = q
        num = c
        while c != num:
            num + 1
            u = q + val[0] * num
        return u


def evaluarnum(numero):
    val = [numero]
    ucien, udec, uni = ["C", "CD", "D", "CM"], ["X", "XL", "L", "XC"], ["I", "IV", "V", "IX"]
    m, c, d, u = numero // 1000, numero // 100 % 10, numero // 10 % 10, numero % 10

    if numero >= 1000:
        um = "M" * m
        ac = conversor(c, ucien)
        ad = conversor(d, udec)
        au = conversor(u, uni)
        return um + ac + ad + au

    elif 1000 > numero >= 100:
        ac = conversor(c, ucien)
        ad = conversor(d, udec)
        au = conversor(u, uni)
        return ac + ad + au

    elif numero < 100:
        ad = conversor(d, udec)
        au = conversor(u, uni)
        return ad + au
    else:
        au = conversor(u, uni)
        return au


n = 500
romano = evaluarnum(n)
print(romano)
