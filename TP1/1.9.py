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

import random


def cantidadNaranjas(naranjasprocesadas):
    cajon = []
    naranja = random.randint(150, 350)
    registradas = 0
    while registradas < naranjasprocesadas:
        cajon.append(naranja)
        naranja = random.randint(150, 350)
        registradas += 1
    return cajon


def crearCajones(naranjasprocesadas):
    unCajon = []
    CajonJugo = []
    cajonesapilados = 0
    njugo = 0
    nencajon = 0

    for naranja in range(len(naranjasprocesadas) + 1):  # itera en cantidad de naranjas ingresadas
        if 200 <= naranjasprocesadas[naranja - 1] <= 300:
            unCajon.append(naranjasprocesadas[naranja - 1])  # se agrega la naranja al cajon
            nencajon = nencajon + 1
        elif naranjasprocesadas[naranja - 1] < 199 or naranjasprocesadas[naranja - 1] >= 301:  #naranjas tipo jugo
            CajonJugo.append(naranjasprocesadas[naranja - 1])
            njugo = njugo + 1

    for item in range(0, len(unCajon) + 1, 100):
        cajonesapilados = cajonesapilados + 1

    if nencajon >= 100:
        proximocajon = 100 - (nencajon - 100)
        print("naranjas a completar otro cajon", proximocajon)

    print(nencajon, " naranjas de cosecha")
    # print("cajon cosecha contiene", unCajon) array de naranjas de cosecha
    print(njugo, " naranjas de jugo")  # naranjas de jugo
    # print("cajon jugo contiene ", njugo, CajonJugo)
    print("cajones de cosecha", cajonesapilados)
    transportarCosecha(nencajon,unCajon)

def transportarCosecha(naranjasencajones,unCajon):
    pesototalcajones = 0
    for naranja in range(naranjasencajones):
        pesototalcajones = pesototalcajones+ unCajon[naranja-1]
    print(pesototalcajones)
    if 400000 <= pesototalcajones <= 500000: #500000 es el maximo pero 400000 es el 80%
        print("el camion saldra. Pesa", pesototalcajones)
    elif pesototalcajones < 400000:
        print("el camion no tiene suficiente peso en naranjas para salir")
    else:
        excedente = pesototalcajones-400000
        print("el camion no puede transportar todo el peso,", pesototalcajones,end=" ")
        print(".Quedaran en espera ",excedente," en peso para el proximo camion")

naranjasprocesadas = int(input("Ingrese cantidad de naranjas a procesar: "))
cajones = cantidadNaranjas(naranjasprocesadas)
crearCajones(cajones)
