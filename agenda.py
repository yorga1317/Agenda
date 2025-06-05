import json
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
     
import os 
def limpiarConsola():
    os.system("cls" if os.name == "nt" else "clear")

def enterParaContinuar(mensaje: str = "Enter para continuar..."):
    input(mensaje)

def CrearContactos():
    print("\n--- Agregar nuevo libro ---")
    ID = input("Ingrese ID de Contacto: ")
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
    leerContactojson("usuario.json", bibliotecaDeContactos)
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
    ID_buscar = input("Ingrese el ID del contacto que quieras actualizar: ")
    for Contacto in bibliotecaDeContactos["Contacto"]:
        if Contacto["ID"] == ID_buscar:
            print(f"Contacto Encontrado: {Contacto["Nombre"]}")
            print(f"---Escriba el nuevo valor o Precione enter para no cambiar---")
            actualizarContactosjson("usuario.json", bibliotecaDeContactos)
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_telefono= input("Nuevo telefono: ")
            nueva_email = input("Nueva email: ")
                    
                    
            if nuevo_nombre.strip() != "":
                bibliotecaDeContactos["Nombre"] = nuevo_nombre
            if nuevo_telefono.strip() != "":
                bibliotecaDeContactos["Telefono"] = nuevo_telefono
            if nueva_email.strip() != "":
                bibliotecaDeContactos["Email"] = nueva_email
                    
            print("\nContactos actualizado correctamente.\n")
            return
        print("No se encontró ningún contacto con ese ID.\n")
bibliotecaDeContactos = {
    "Contacto": []
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
            pass
        elif opcion == 5:
            break
        else: 
            print("No sea toche hermano elija una opcion validad :) ")
            pass
        enterParaContinuar("Enter para salir...")
        limpiarConsola()
    except:
        print("Manda huevo")
    