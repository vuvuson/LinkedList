class Client:
    def __init__(self, name, phone, birth):
        self.name = name
        self.phone = phone
        self.birth = birth

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, birth: {self.birth}"
    
class BoudreauxShop:
    def __init__(self):
        self.clients = []

    def add_client(self, name, phone, birth):
        new_client = Client(name, phone, birth)
        self.clients.append(new_client)
        print("You've added a new client!")

    def display_client(self):
        if not self.clients:
            print("No clients to display.")
        else:
            for client in self.clients:
                print(client)

    def search_client(self, name):
        found = False
        for client in self.clients:
            if client.name.lower() == name.lower():
                print(client)
                found = True
                break
        if not found:
            print(f"No client found with name {name}.")

    def delete_client(self, name):
        for client in self.clients:
            if client.name == name():
                self.clients.remove(client)
                print(f"client {name} has been deleted.")
                return
        print(f"No client found with name {name}")

# Main menu
def main():
    boudreaushop = BoudreauxShop()

    while True:
        print("\n Boudreaux's Babershop")
        print("\n Type a number for the action you wish to perform and then hit Enter.")
        print("\n 1. Add a new client")
        print("\n 2. Display a list of all current clients")
        print("\n 3. Search for a client")
        print("\n 4. Delete a client")
        print("\n 5. Quit")

        action = input("\n What do you want to do? ")

        if action == "1":
            name = input("Provide the client's name: ")
            phone = input("Provide the client's phone number: ")
            birth = input("Provide the client's D.O.B  in MMDDYYYY: ")
            boudreaushop.add_client(name, phone, birth)

        elif action == "2":
            boudreaushop.display_client()

        elif action == "3":
            name = input("Enter the name of the client: ")
            boudreaushop.search_client(name)

        elif action =="4":
            name = input("Enter the name of client you want to delete: ")
            boudreaushop.delete_client(name)

        elif action =="5":
            print("Bye!")
            break

        else:
            print("I'm sorry, that is not an allow action.")

if __name__ == "__main__":
    main()