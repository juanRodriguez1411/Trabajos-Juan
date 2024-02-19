import random

secreto = random.randint(1,10)

Numero = int(input("Adivininar el numero entre 1 a 10"))

while Numero != secreto:
    if Numero < secreto:
        print("El numero es mayor")
    else:
        print("El numero es menor")

    Numero = int(input("Intenta de nuevo"))

print("Felicidades adivinaste el numero secreto :", secreto)
