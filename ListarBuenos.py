#definir las listas
nombres=[]
notas=[]
amejor=[]
eliminar=[]
mb=0
b=0
iN=0

for x in range(1,5):
    nom = input(f"Por favor ingrese el nombre del alumno {x}:")
    nombres.append(nom)
    no = int(input(f"Por favor ingresa las notas del alumno  {x}:"))
    notas.append(no)

for y in range (len(nombres)):
    print(nombres[y])
    print(notas[y])

    if notas[y]>=8:
        print("Alumno muy  bueno")
        mb+=1
        amejor.append(nombres[y])
    else:
        if notas[y]>=4:
            print("Alumno bueno")
            b+=1
        else:
            print("Alumno no aprueba materia")
            iN+=1

for z in len(notas):
    if notas[z]>=4 and notas[z]<=7:
        notas.pop(z)
        nombres.pop(z)
        eliminar.append(z)
for d in sorted(eliminar,reverse=True):
    notas.pop[d]
    nombres.pop[d]


print("Cantidad de alumnos excelentes",mb)
print("Nombre de los alumnos excelentes",amejor)
print("Listado de alumnos con notas entre 4 y 7")
print()



