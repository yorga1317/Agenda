import json
import os 

def escribirEnJson(nombreArchivo: str, datos: dict):
    with open(nombreArchivo, "w") as file:
        json.dump(datos, file, indent=4)

def leerContactojson(nombreArchivo: str, datos: dict):
    with open(nombreArchivo, "r") as file:
        leerArchivo = json.load(file)
        return leerArchivo.get("Contacto", [])

def actualizarContactosjson(nombreArchivo: str, datos: dict):
    with open(nombreArchivo, "w") as file:
        json.dump(datos, file, indent=4)
     
def limpiarConsola():
    os.system("cls" if os.name == "nt" else "clear")

def enterParaContinuar(mensaje: str = "Enter para continuar..."):
    input(mensaje)

def CrearContactos():
    print("\n--- Agregar nuevo contacto ---")

    ID = int(input("Ingrese ID de Contacto: "))
    Nombre = input("Ingrese nombre del contacto: ")
    Telefono = input("Ingrese telefono del contacto: ")
    Email = input("Ingrese email del contacto: ")

    nuevoContacto = {
        "ID": ID,
        "Nombre": Nombre,
        "Telefono": Telefono,
        "Email": Email
    }
    bibliotecaDeContactos["Contacto"].append(nuevoContacto)
    escribirEnJson("usuario.json", bibliotecaDeContactos)
    print(f"\nEl contacto '{Nombre}' se ha agregado correctamente.\n")

def leerContactos():
    print("\n---lista de contactos---")
    contactos = bibliotecaDeContactos["Contacto"]
    if not contactos:
        print("no hay contactos registrados")
    else:
        for contacto in contactos:
            print(f"\nID: {contacto['ID']}")
            print(f"Nombre: {contacto['Nombre']}")
            print(f"Teléfono: {contacto['Telefono']}")
            print(f"Email: {contacto['Email']}")
            print("")

def actualizarContacto():
    try:
        ID_buscar = int(input("Ingrese el ID del contacto que quieras actualizar: "))
    except ValueError:
        print("ID inválido. Debe ser un número entero.")
        return

    encontrado = False
    for Contacto in bibliotecaDeContactos["Contacto"]:
        if Contacto["ID"] == ID_buscar:
            print(f"Contacto Encontrado: {Contacto['Nombre']}")
            print(f"---Escriba el nuevo valor o presione Enter para no cambiar---")
            
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_telefono = input("Nuevo telefono: ")
            nueva_email = input("Nueva email: ")
                    
            if nuevo_nombre.strip() != "":
                Contacto["Nombre"] = nuevo_nombre
            if nuevo_telefono.strip() != "":
                Contacto["Telefono"] = nuevo_telefono
            if nueva_email.strip() != "":
                Contacto["Email"] = nueva_email

            actualizarContactosjson("usuario.json", bibliotecaDeContactos)        
            print("\nContacto actualizado correctamente.\n")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró ningún contacto con ese ID.\n")

def eliminarContacto():
    try:
        ID_buscar = int(input("Ingrese el ID del contacto que deseas eliminar: "))
    except ValueError:
        print("ID inválido. Debe ser un número entero.")
        return

    for i, contacto in enumerate(bibliotecaDeContactos["Contacto"]):
        if contacto["ID"] == ID_buscar:
            print(f"Contacto encontrado: {contacto['Nombre']}")
            confirmar = input("¿Está seguro que deseas eliminarlo? (si/no): ")
            if confirmar.lower() == "si":
                bibliotecaDeContactos["Contacto"].pop(i)
                actualizarContactosjson("usuario.json", bibliotecaDeContactos)
                print("Contacto eliminado correctamente.")
            else:
                print("Operación cancelada.")
            return
    print("No se encontró ningún contacto con ese ID.")


bibliotecaDeContactos = {
    "Contacto": leerContactojson("usuario.json", {})
}
menu = '''
+------------------------------------------------------+
| _______  _______  _______  _        ______   _______ |
|(  ___  )(  ____ \(  ____ \( (    /|(  __  \ (  ___  )|
|| (   ) || (    \/| (    \/|  \  ( || (  \  )| (   ) ||
|| (___) || |      | (__    |   \ | || |   ) || (___) ||
||  ___  || | ____ |  __)   | (\ \) || |   | ||  ___  ||
|| (   ) || | \_  )| (      | | \   || |   ) || (   ) ||
|| )   ( || (___) || (____/\| )  \  || (__/  )| )   ( ||
||/     \|(_______)(_______/|/    )_)(______/ |/     \||
+------------------------------------------------------+
+------------------------------------------------------+
|             1. Crear contacto                        |
|             2. leer contactos                        |  
|             3. Actualizar Contacto                   |  
|             4. Eliminar Contacto                     |  
|             5. salir                                 |
+------------------------------------------------------+
'''
while True:
    limpiarConsola()
    print(menu)
    try:
        opcion = int(input("Ingrese la opcion que sea de tu utilidad: "))
        if opcion == 1:
            CrearContactos()
        elif opcion == 2:
            leerContactos()
        elif opcion == 3:
            actualizarContacto()
        elif opcion == 4:
            eliminarContacto()
        elif opcion == 5:
            print("saliendo ...")
            break
        else: 
            print("No sea toche hermano elija una opcion validad :) ")
        enterParaContinuar()
    except:
        print("Ocurrió un error:")
        enterParaContinuar()
        limpiarConsola()
    