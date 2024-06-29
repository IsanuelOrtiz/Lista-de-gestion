import csv

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def is_palindrome(self):
        return self.name.lower() == self.name.lower()[::-1]

class ContactManager:
    def __init__(self):
        self.contacts = []  # Inicializar la lista de contactos

    def add_contact(self, name, phone, email):
        self.contacts.append(Contact(name, phone, email))

    def edit_contact(self, index, name, phone, email):
        if 0 <= index < len(self.contacts):
            self.contacts[index].name = name
            self.contacts[index].phone = phone
            self.contacts[index].email = email

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]

    def search_contacts(self, name):
        return [contact for contact in self.contacts if name.lower() in contact.name.lower()]

    def find_extreme_names(self):
        if not self.contacts:
            return None, None

        longest = max(self.contacts, key=lambda contact: len(contact.name))
        shortest = min(self.contacts, key=lambda contact: len(contact.name))
        return longest, shortest

    def export_to_csv(self, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['Name', 'Phone', 'Email'])
            for contact in self.contacts:
                csvwriter.writerow([contact.name, contact.phone, contact.email])
        print(f"Datos exportados a {filename}")

def main():
    manager = ContactManager()

    while True:
        print("1. Agregar contacto")
        print("2. Editar contacto")
        print("3. Eliminar contacto")
        print("4. Buscar contacto")
        print("5. Verificar palíndromo")
        print("6. Encontrar nombres extremos")
        print("7. Exportar a CSV")
        print("8. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            name = input("Nombre: ")
            phone = input("Teléfono: ")
            email = input("Email: ")
            manager.add_contact(name, phone, email)
        elif choice == '2':
            index = int(input("Índice del contacto a editar: "))
            name = input("Nuevo nombre: ")
            phone = input("Nuevo teléfono: ")
            email = input("Nuevo email: ")
            manager.edit_contact(index, name, phone, email)
        elif choice == '3':
            index = int(input("Índice del contacto a eliminar: "))
            manager.delete_contact(index)
        elif choice == '4':
            name = input("Nombre a buscar: ")
            results = manager.search_contacts(name)
            for contact in results:
                print(f"{contact.name}, {contact.phone}, {contact.email}")
        elif choice == '5':
            index = int(input("Índice del contacto para verificar palíndromo: "))
            if 0 <= index < len(manager.contacts):
                if manager.contacts[index].is_palindrome():
                    print("El nombre es un palíndromo.")
                else:
                    print("El nombre no es un palíndromo.")
            else:
                print("Índice fuera de rango.")
        elif choice == '6':
            longest, shortest = manager.find_extreme_names()
            if longest and shortest:
                print(f"Nombre más largo: {longest.name}")
                print(f"Nombre más corto: {shortest.name}")
            else:
                print("No hay contactos para analizar.")
        elif choice == '7':
            filename = 'Usuarios.csv'
            manager.export_to_csv(filename)
        elif choice == '8':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
