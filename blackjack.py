import sys
from random import sample, shuffle, choice

cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
}

print("")
print(f"Las cartas y sus puntos son: {cartas}.\n" )         #Se enseñan las cartas y su puntuación.


lista_cartas = list(cartas)                             
carta = choice(lista_cartas)                            #Se elige aleatoriamente las dos cartas del jugador
carta2 = choice(lista_cartas)
puntos = cartas[carta]                                  #Determinamos las puntuaciones de las dos cartas por separado del jugador
puntos2 = cartas[carta2]
puntosjugador = puntos + puntos2

print(f"Tus cartas son {carta} con valor {puntos} y {carta2} con valor {puntos2}. Tus cartas suman {puntos + puntos2}.\n")
                                                        #Acabamos de printear los puntos y las cartas del jugdor

lista_cartas = list(cartas)
carta = choice(lista_cartas)                            #Se elige aleatoriamente las dos cartas de la banca
carta2 = choice(lista_cartas)
puntosbanca = cartas[carta] + cartas[carta2]            #Se suma directamente las puntuaciones de las dos cartas de la banca juntas

print(f"Las carta de la banca son {carta} y {carta2}. Las cartas suman: {puntosbanca} puntos.\n")
                                                        #Acabamos de printear las dos cartas y su puntuacion sumada de la banca

if puntosbanca < puntosjugador:                         #Comparamos las puntuaciones de los dos y decimos quien ha ganado
    print("¡¡Has ganado!!")
elif puntosbanca == puntosjugador:
    print("Empate bro.")
else: 
    print("Has perdido... :(\n")