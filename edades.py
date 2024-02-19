



suma = 0
suma1 = 0
suma2 = 0

for i in range(6):
    mañana = int(input("Ingrese la edad del estudiante del turno mañana: "))
    suma=suma+mañana
   
for i in range(7):
    tarde = int(input("Ingrese la edad del estudiante del turno tarde: "))
    suma1=suma1+tarde
    
for i in range(12):
    noche = int(input("Ingrese la edad del estudiante del turno noche: "))
    suma2=suma2+noche

promañana=suma/6
promtarde=suma1/7
promnoche=suma2/12

promfinal = suma + suma1 + suma2/23

print("El promedio de las edades del turno de la mañana es: ",promañana)
print("El promedio de las edades de los estudiantes de la tarde es: ",promtarde)
print("El promedio de las edades de los estidoantes de la noche es: ",promnoche)
print("El promedio de edades final de los estudiantes es: ",promfinal)

    




