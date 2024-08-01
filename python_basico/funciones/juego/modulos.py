
from aletorio import generar

numero_a_adivinar = generar(1,10)

print("¡Bienvenido al juego de Adivina el Número!")
print("Estoy pensando en un número entre 1 y 10.")

while True:
    intento = int(input("Introduce tu intento: "))

    if intento < numero_a_adivinar:
        print("Demasiado bajo. Intenta de nuevo.")
    elif intento > numero_a_adivinar:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print("¡Felicidades! Adivinaste el número.")
        break
