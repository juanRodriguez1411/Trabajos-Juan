def calcular_sueldos(empleados):
    sueldos_entre_1_y_3_millones = 0
    sueldos_mas_de_3_millones = 0
    cantidad_empleados_entre_1_y_3_millones = 0
    cantidad_empleados_mas_de_3_millones = 0

    for sueldo in empleados:
        if 1_000_000 <= sueldo < 3_000_000:
            cantidad_empleados_entre_1_y_3_millones += 1
            sueldos_entre_1_y_3_millones += sueldo
        elif sueldo >= 3_000_000:
            cantidad_empleados_mas_de_3_millones += 1
            sueldos_mas_de_3_millones += sueldo

    total_gastos = sum(empleados)
    
    return (cantidad_empleados_entre_1_y_3_millones, cantidad_empleados_mas_de_3_millones, total_gastos)

empleados = [int(input(f"Ingrese el sueldo del empleado {i + 1}: ")) for i in range(int(input("Ingrese la cantidad de empleados: ")))]

resultado = calcular_sueldos(empleados)

print(f"Empleados que cobran entre 1.000.000 y 3.000.000: {resultado[0]}")
print(f"Empleados que cobran más de 3.000.000: {resultado[1]}")
print(f"Total de gastos en sueldos: {resultado[2]}")