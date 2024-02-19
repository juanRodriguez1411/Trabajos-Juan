def inicio():

    print("MENU PRINCIPAL")
    print("seleccione la opcion correcta:")
    print("1. operacin sumar")
    print("2 Operacion resta")
    print("3 operacion iltiplicar")
    print("4 operacion dividir")

def main():
    while True:
        opcion = int(input("Seleccione la opcion"))
        if opcion == 1:
            print("Ha seleccionado la suma ")
            num1 = int(input("Ingresar e 1 numero"))
            num2 = int(input("Ingresar el 2 numero"))
            sumar = num1+num2
            print("El resultado de la suma es: ",sumar)
         elif opcion == 2:
            print("has seleccionado la resta")
            num1 = int(input("ingresar el numero 1"))
            num2 = int(input("ingresar el numero 2"))
            restar = num1-num2
            print("el resultado de la suma es: ",restar)
        elif opcion == 3:
            print("has seleccionado la multiplicacion")
            num1 = int(input("ingresar el numero 1"))
            num2 = int(input("ingresar el numero 2"))
            multipli = num1*num2
            print("el resultado de la suma es: ",multipli)
        elif opcion == 4:
            print("has seleccionado la divicion")
            num1 = int(input("ingresar el numero 1"))
            num2 = int(input("ingresar el numero 2"))
            divicion = num1/num2
            print("el resultado de la suma es: ",divicion)
        else:
            print("opcion no valida")
main()