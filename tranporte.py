nombre=[]
kms=[]

km=0
dias_semana=["L","M","I","J","V","S","D"]


for x in range(4):
    nom= input("Ingresar el nombre del conductor")
    nombre.append(nom)
    L = int(input(f"Ingresar kilometros realizados el lunes"))
    kms.append(L) 
    M =  int(input(f"Ingresar kilometros realizados el Martes"))
    kms.append(M) 
    I = int(input(f"Ingresar kilometros realizados el Miercoles"))
    kms.append(I) 
    J =  int(input(f"Ingresar kilometros realizados el Jueves"))
    kms.append(J) 
    V =  int(input(f"Ingresar kilometros realizados el Viernes"))
    kms.append(V)
    kms.append(I) 
    S =  int(input(f"Ingresar kilometros realizados el Sabado"))
    kms.append(S) 
    D =  int(input(f"Ingresar kilometros realizados el Domingo"))
    kms.append(D)
    
totalkms=sum(kms[nombre].values())
print(f"{nombre} Ha recorrido un total de {totalkms}kilometro esta semana.\n")



    
for y in range (len(nombre)):
    print(nombre[y])
    print(kms[y])

    if kms[y]>=1:
        print("Kilometros realizados")
        km+=1
        kms.append(nombre[y])


        