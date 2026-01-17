usuarios = {"Carlos44": 100000,
            "Tamalito4": 500000,
            "Ana23": 2500000}
print("Bienvenido al Cajero Automático:")

def consultar_saldo(usuario):
    print(f"Saldo de {usuario} es: {usuarios[usuario]}")
def depositar_dinero(usuario,ingresar_dinero):

    usuarios[usuario]+=ingresar_dinero
    print("Dinero ingresado con exito\n")
def retirar_dinero(usuario,retirar):
    usuarios[usuario] -= retirar
    print("Dinero retirado con exito\n")
usuario_actual = ""
while True:
    while True:
        usuario = input("Ingrese su nombre de usuario: ")
        if usuario in usuarios:
            usuario_actual = usuario
            print("Usuario correcto")
            break;
        else:
            print("Usuario incorrecto, intentelo de nuevo")
    while True:
        print("""1. Consultar saldo
2. Depositar dinero
3. Retirar dinero
4. Salir""")
        try:
            opcion = int(input("Ingrese la opción que desea: "))
        except ValueError:
            print("Error, Ingrese una opción valida")
            continue
        if opcion == 1:
            consultar_saldo(usuario_actual)
        elif opcion == 2:
            while True:
                try:
                    ingresar_dinero = float(input("Cuanto dinero va a ingresar? "))
                except ValueError:
                    print("Error, Ingrese una cantidad valida")
                    continue
                if ingresar_dinero > 0:
                    depositar_dinero(usuario_actual,ingresar_dinero)
                    break
                else:
                    print("No se pudo ingresar el dinero con exito\n")
                    break
        elif opcion == 3:
            while True:
                try:
                    retirar = float(input("Cuanto dinero va a retirar?"))
                except ValueError:
                    print("Error, Ingrese una cantidad valida")
                    continue
                if retirar > usuarios[usuario_actual] or retirar <= 0:
                    print("No se pudo retirar el dinero con exito\n")
                    break
                else:
                    retirar_dinero(usuario_actual,retirar)
                    break;
        elif opcion == 4:
            print("Cerrando sesion. ¡Hasta luego!")
            break
        else:
            print("Opcion no válida\n")
    print("Siguiente usuario:")