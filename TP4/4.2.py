# Leer una cadena de caracteres e imprimirla centrada en pantalla.
# Suponer que la misma tiene 80 columnas.

def centrar(cadena):
    extremos=(80-len(cadena))//2
    relleno=" "*extremos
    centrada ="|"+relleno+cadena+relleno+"|"
    return centrada


cadena = input("Ingrese la cadena que quiere centrar")
centrado = centrar(cadena)
print(centrado)
# Yo nunca me pierdo...son los demás los que no me encuentran.