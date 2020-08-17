'''Resolver el siguiente problema diseñando y utilizando funciones:
Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso para poder cargar el camión de reparto. La empresa cuenta con N camiones, y
cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón
caben 100 naranjas con un peso entre 200 y 300 gramos cada una. Si el peso de
alguna naranja se encuentra fuera del rango indicado, se clasifica para procesar
como jugo. Se solicita desarrollar un programa para ingresar la cantidad de naranjas cosechadas
e informar cuántos cajones se pueden llenar, cuántas naranjas son para jugo y
si hay algún sobrante de naranjas que deba considerarse para el siguiente reparto.
 Simular el peso de cada unidad generando un número entero al azar entre 150 y 350.
Además, se desea saber cuántos camiones se necesitan para transportar la cosecha,
considerando que la ocupación del camión no debe ser inferior al 80%; en
caso contrario el camión no serán despachado por su alto costo'''


# camiones= n??? max 500 .min 400 toneladas
# cajones 100 naranjas entre 200 y 300 gramos
# naranjas jugo ->150 a 200 ,301 a 350
# cantnaranjas


def crearCajones(naranjasprocesadas):
    unCajon = []
    cajonesTotales = []
    njugo = 0
    for naranja in range(naranjasprocesadas + 1):
        if 200 < naranja < 300:  # naranja>200 and naranja<300
            unCajon.append(naranja)
        else:
            njugo = +1
    return njugo, unCajon


def calcularPesoCajones(cajones):
    pesototalcajones = 0
    camiones = 0
    for cajon in range(cajones + 1):
        pesototalcajones += cajon
    cantidadCamiones(pesototalcajones)


def cantidadCamiones(pesototal):
    camion = 0
    enespera = 0
    if pesototal >= 5000:
        camion += 1
    elif pesototal <= 3999:
        enespera += 1  # el peso del camion es insuficiente para salir
    return camion, enespera


def transportarCosecha(camion, enespera):

    camionesllenos = []
    camionesllenos.append(camion)
    camionesenespera = []
    camionesllenos.append(enespera)
    if len(camionesllenos) > 0:
        print("se necesitan transportar", len(camionesllenos),"camiones")
    if len(camionesenespera) > 0:
        print("se encuentran en espera", len(camionesenespera), "camiones")


naranjasprocesadas = 200
