def show_menu():
    print("\n--- Menu ---")
    print("1. Agregar")
    print("2. Cambiar")
    print("3. Buscar")
    print("4. Borrar")
    print("5. Mostrar lista")
    print("6. Salir")

def add_contact(agenda):
    name = input("Ingrese el nombre del contacto: ")
    if name in agenda:
        print("Este contacto ya existe. Use la opcion para cambiar.")
    else:
        phone = input("Ingresar el numero de telefono ")
        agenda[name] = phone
        print("Contact added.")

def change_contact(agenda):
    name = input("Ingrese el nombre del contacto a cambiar: ")
    if name in agenda:
        print(f"Telefono actual de {name}: {agenda[name]}")
        new_phone = input("Ingrese el nuevo telefono: ")
        agenda[name] = new_phone
        print("Numero de telefono actualizado.")
    else:
        print("Contacto equivocado.")

def search_contacts(agenda):
    search_query = input("Ingrese un nombre para buscar: ")
    matches = [name for name in agenda if name.startswith(search_query)]
    if matches:
        print("Contactos encontrados:")
        for name in matches:
            print(f"{name}: {agenda[name]}")
    else:
        print("No se encontro vuelva a intentar.")

def delete_contact(agenda):
    name = input("Ingrese el nombre del contacto a eliminar: ")
    if name in agenda:
        confirm = input(f"Estas seguro que deseas eliminar {name}? (y/n): ")
        if confirm.lower() == 'y':
            del agenda[name]
            print("Contacto eliminado.")
    else:
        print("Nombre no encontrado.")

def show_items(agenda):
    if agenda:
        print("Contactos en la agenda:")
        for name, phone in agenda.items():
            print(f"{name}: {phone}")
    else:
        print("No hay contactos en la agenda.")

agenda = {}
while True:
    show_menu()
    option = input("Selecione una opcion: ")
    if option == '1':
        add_contact(agenda)
    elif option == '2':
        change_contact(agenda)
    elif option == '3':
        search_contacts(agenda)
    elif option == '4':
        delete_contact(agenda)
    elif option == '5':
        show_items(agenda)
    elif option == '6':
        print("saliendo la agenda.")
        break
    else:
        print("Opcion invalida. Intente nueva mente.")

