def registrar():
    #definimos el diccionario 
    agenda={}
    respuesta ="s"

    while respuesta =="s":
        fecha = input("Ingrese la fecha con formato dd/mm/aa :")
        listas=[]
        while respuesta == "s":
            hora = input("ingresar la hora de la actividad : h/m")
            actividad = input("Ingresar el nombre de la actividad")
            listas.append((hora,actividad))
            respuesta =input("Desea ingresar una actividad para la misma fecha s/n :")
        agenda[fecha]=listas
        respuesta = input("Desea ingresa otra fecha s/n :")
    return agenda
def mostrar(agenda):
    print("Listado de la agenda")
    for fecha in agenda:
        print("Para la fecha :",fecha)
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)
def consultarxfecha(fecha):
    fecha = input("Ingresar la fecha que desea consultar sus actividades")
    if fecha in agenda:
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)
    else:
        print("No existe actividad para fecha ingresada")
agenda=registrar()
mostrar(agenda)
consultarxfecha(agenda)