"""
Escribir un programa que vaya solicitando al usuario que ingrese nombres:
a) Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar el telefono y, 
opcionalmente, permitir modificarlo si no es correcto.
b) Si el nombre no se encuentra, debe permitir ingresar el telefono correspondiente.
El usuario puede usar "*" para salir del programa.
"""

agenda = {"Maria":12412, "Juan":75283, "Sergio":314912, "Carla":174812, "Roberto":523041}
def actualizar_agenda(agenda):
    """ """
    corte = ""
    while corte!="*":
        nombre = ingresar_nombre()
        if nombre in agenda:
            print(agenda[nombre])
            cambiar_numero(nombre, agenda)
        else:
            numero = ingresar_numero()
            agenda[nombre] = numero
            print("Contacto creado.\n", nombre, numero)
        corte = input("Si desea cerrar la agenda, ingrese *")
    return agenda


def ingresar_nombre():
    """Pide un nombre y si cumple con las validaciones, lo devuelve."""
    nombre = input("Ingrese un nombre:\n")
    while (not nombre.isalpha()) or (len(nombre) == 0):
        nombre = input("Debe ingresar un nombre valido:\n")
    
    return nombre


def elegir_cambiar_numero():
    """Devuelve true en caso de que se quiera cambiar el numero y false en caso contrario."""
    decision = input("\nDesea modificar el numero de contacto? si / no: ")
    while (decision.lower() != "si" and decision.lower() != "no"):
        decision = input("\nDebe ingresar si o no: ")
    return decision.lower() == "si"


def cambiar_numero(nombre_contacto, agenda):
    """Recibe un nombre de contacto y una agenda, y permite cambiar el numero."""
    desea_cambiar_numero = elegir_cambiar_numero()
    
    if desea_cambiar_numero:
        numero_contacto = ingresar_numero()
        agenda[nombre_contacto] = numero_contacto
        print("Contacto actualizado.\n", nombre_contacto, numero_contacto)


def ingresar_numero():
    """Pide ingresar un numero, lo valida y lo devuelve."""
    numero = "a"
    while numero.isalpha():
        numero = input("\nIngrese un nuevo numero de contacto: ")
    
    return confirmar_numero(numero)


def confirmar_numero(numero_contacto):
    """Recibe un numero de contacto y le pide al usuario que confirme."""
    numero = numero_contacto
    print("\nEl numero de contacto ingresado es: {}".format(numero))
    confirmacion = input("\nConfirmar? si o no: ")
    while (confirmacion.lower() != "si" and confirmacion.lower() != "no"):
        confirmacion = input("\nDebe ingresar si o no: ")
    if confirmacion == "no":
        numero = ingresar_numero()
    
    return numero

    

#actualizar_agenda(agenda)













