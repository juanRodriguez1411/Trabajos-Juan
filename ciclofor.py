n = int(input("Ingrese # de empleados"))
cont = 0
cont1 = 0
gasto = 0
for ini in range(n):
    sueldo = float(input("Ingresar el valor sueldo del  empleado"))
    gasto = gasto+sueldo
    if sueldo >=1300.000 and sueldo <=3000.000:
        cont+=1
    elif sueldo >3000.000:
        cont1+=1
print("Los gastos de la empresa total ", gasto)
print("Empleados que ganan entre 1300.000 y 3000.000 son: ",cont)
print("Empleados que ganan mas de 3000.000 son: ",cont1)