def registrar():
    notas={}
    respuestas="s"
    while respuestas=="s":
        alumno = input("Ingrese su Nombre :")
        lista=[]
        while respuestas == "s":
            nota = int(input("Ingrese las notas optenidas en su clase"))
            lista.append((notas,alumno))
            respuestas =input("Desea ingresar otra nota s/n :")
        notas[nota]=lista
    return notas
def consultar(alumno):
    alumno = input("Ingrese el nombre del alumno que desea consultar")
    if alumno in notas:
        for nota in notas [alumno]:
            print (nota,alumno)
    else:
        print("Alumno no encontrado")
notas=registrar()
consultar(notas)