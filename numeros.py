Numero = [int(input(f"Ingresar 10 numeros {i+1}:"))
for i in range (10)]

acum = 0

prom = sum(Numero)/len(Numero)
acum=acum+Numero

print(f"El promedio de los 10 numeros es : {prom}")