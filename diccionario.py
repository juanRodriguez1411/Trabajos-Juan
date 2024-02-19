persona = {
    "Nombre":"Juan Esteban",
    "Apellido":"Rodriguez Mora",
    "Estatura":1.67,
    "Edad":17,
    "Email":"esteban14juanQgmail.com",
    "CiudadNac":"Bogota",
    "Genero":["Masculino","Terreneitor","helicoptero yamaha"]
}
  
print(persona)
#mostrarun elemento al diccionario
print("El nombre de la persona es:", {persona["Nombre"]})
#agregar elemento del diccionario
persona["Telefono"]=3219344399
print(persona)
"modificar elemento del diccionario"
persona["Telefono"]=3102109232
print(persona)
#modificar la clave del elemento
persona["Celular"] = persona.pop("Telefono")
print(persona)
#Eliminar un elemento del diccionario
del persona["Celular"]
print(persona)

#Interar los item de las claves y valores
for clave,valor in persona.items():
    print(clave , ": " , valor)