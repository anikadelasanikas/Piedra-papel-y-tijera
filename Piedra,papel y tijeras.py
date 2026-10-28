import random

def piedra(jugada_de_usuario):
    if jugada_de_usuario == "tijera":
        print("Gana la piedra")
    elif jugada_de_usuario == "papel":
        print("Pierde la piedra")
    else:
        print("Empate")

def tijera(jugada_de_usuario):
    if jugada_de_usuario == "piedra":
        print("Pierde la tijera")
    elif jugada_de_usuario == "papel":
        print("Gana la tijera")
    else:
        print("Empate")

def papel(jugada_de_usuario):
    if jugada_de_usuario == "piedra":
        print("Gana el papel")
    elif jugada_de_usuario == "tijera":
        print("Pierde el papel")
    else:
        print("Empate")

def piedra_oponente(jugada_de_oponente):
    if jugada_de_oponente == "tijera":
        print("Gana la piedra")
    elif jugada_de_oponente == "papel":
        print("Pierde la piedra")
    else:
        print("Empate")

def tijera_oponente(jugada_de_oponente):
    if jugada_de_oponente == "piedra":
        print("Pierde la tijera")
    elif jugada_de_oponente == "papel":
        print("Gana la tijera")
    else:
        print("Empate")

def papel_oponente(jugada_de_oponente):
    if jugada_de_oponente == "piedra":
        print("Gana el papel")
    elif jugada_de_oponente == "tijera":
        print("Pierde el papel")
    else:
        print("Empate")

jugada_de_usuario = input("Elige piedra, papel o tijera (todo en minúscula: ")

jugada_oponente = random.choice(["piedra", "papel", "tijera"])

print(f"El oponente eligió: {jugada_oponente}")

if jugada_de_usuario == "piedra":
    piedra(jugada_de_usuario)
    piedra_oponente(jugada_oponente)

elif jugada_de_usuario == "papel":
    papel(jugada_de_usuario)
    papel_oponente(jugada_oponente)

elif jugada_de_usuario == "tijera":
    tijera(jugada_de_usuario)
    tijera_oponente(jugada_oponente)

else:
    print("Jugada no válida") 
    
 
    