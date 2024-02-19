num_personas = int(input("Ingrese el número de personas: "))


suma_alturas = 0


for i in range(num_personas):
    altura = float(input(f"Ingrese la altura de la persona {i + 1} en centímetros: "))
    suma_alturas += altura

altura_promedio = suma_alturas / num_personas


print(f"La altura promedio de las {num_personas} personas es: {altura_promedio:.2f} centímetros")