frase = input("Por favor ingrese una frase")
letra = input("Por favor ingrese la letra a buscar")
cletra = 0 

for i in frase:
    if i == letra:
        cletra += 1

print("La letra '%s' aparece %2i en la frase '%s'."%(letra,cletra,frase))