import random

# Función para obtener la elección del usuario
def obtener_eleccion_usuario():
    eleccion = input("Elige piedra, papel o tijera: ").lower()
    while eleccion not in ["piedra", "papel", "tijera"]:
        eleccion = input("Eleccion no válida. Elige piedra, papel o tijera: ").lower()
    return eleccion

# Función para obtener la elección de la máquina
def obtener_eleccion_maquina():
    return random.choice(["piedra", "papel", "tijera"])

# Función para determinar el ganador
def determinar_ganador(eleccion_usuario, eleccion_maquina):
    if eleccion_usuario == eleccion_maquina:
        return "Empate"
    elif (
        (eleccion_usuario == "piedra" and eleccion_maquina == "tijera") or
        (eleccion_usuario == "papel" and eleccion_maquina == "piedra") or
        (eleccion_usuario == "tijera" and eleccion_maquina == "papel")
    ):
        return "Usuario"
    else:
        return "Máquina"

# Función para jugar una partida
def jugar_partida():
    eleccion_usuario = obtener_eleccion_usuario()
    eleccion_maquina = obtener_eleccion_maquina()
    print(f"Usuario elige: {eleccion_usuario}")
    print(f"Máquina elige: {eleccion_maquina}")

    ganador = determinar_ganador(eleccion_usuario, eleccion_maquina)
    if ganador == "Empate":
        print("¡Empate!")
    else:
        print(f"{ganador} gana esta ronda.")

    return ganador

# Función principal del juego
def main():
    puntaje_usuario = 0
    puntaje_maquina = 0

    while True:
        ganador = jugar_partida()

        if ganador == "Usuario":
            puntaje_usuario += 1
        elif ganador == "Máquina":
            puntaje_maquina += 1

        print(f"Puntaje: Usuario {puntaje_usuario} - Máquina {puntaje_maquina}")

        seguir_jugando = input("¿Quieres seguir jugando? (s/n): ").lower()
        if seguir_jugando != "s":
            break

    print("¡Gracias por jugar!")

if __name__ == "__main__":
    main()

