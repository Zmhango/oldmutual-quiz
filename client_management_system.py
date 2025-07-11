import string

# A list to store all client records
clients = []

# Function to add a new client
def add_client():
    client_id = input("Enter client ID: ")
    name = input("Enter client name: ")
    fund = input("Enter Fund: ")
    clients.append({"id": client_id, "name": name, "fund": fund})
    print("Client added successfully!\n")

# Function to view all clients
def view_clients():
    if not clients:
        print("No clients available.\n")
        return
    print("===== CLIENT LIST =====")
    for client in clients:
        print(f"ID: {client['id']} | Name: {client['name']} | Fund: {client['fund']}")
    print(f"Total clients: {len(clients)}\n")

# Function to search for a client
def search_client():
    term = input("Enter search term: ").lower()
    results = [c for c in clients if term in c["name"].lower() or term in c["id"].lower()]
    if results:
        print(f"Found {len(results)} client(s):")
        for c in results:
            print(f"ID: {c['id']} | Name: {c['name']} | Fund: {c['fund']}")
    else:
        print("No Match Found.")
    print()

# Function to edit a client's details
def edit_client():
    client_id = input("Enter client ID to edit: ")
    for client in clients:
        if client["id"] == client_id:
            print(f"Current details - ID: {client['id']} | Name: {client['name']} | Fund: {client['fund']}")
            new_name = input("Enter new name (Enter to keep current Name): ")
            new_fund = input("Enter new Fund (Enter to keep current Fund): ")
            if new_name:
                client["name"] = new_name
            if new_fund:
                client["fund"] = new_fund
            print("Client updated successfully!\n")
            return
    print("Client not found.\n")

# Function to delete a client
def delete_client():
    client_id = input("Enter client ID to delete: ")
    for client in clients:
        if client["id"] == client_id:
            confirm = input(f"Are you sure you want to delete {client['name']}? (y/n): ")
            if confirm.lower() == 'y':
                clients.remove(client)
                print("Client deleted successfully!\n")
            else:
                print("Delete cancelled.\n")
            return
    print("Client not found.\n")

# Main menu loop
def main():
    while True:
        print("=======================================||||||||| CLIENT MANAGEMENT SYSTEM |||||||||=============================================")
        print("1. Add Client")
        print("2. View All Clients")
        print("3. Search Client")
        print("4. Edit Client")
        print("5. Delete Client")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_client()
        elif choice == "2":
            view_clients()
        elif choice == "3":
            search_client()
        elif choice == "4":
            edit_client()
        elif choice == "5":
            delete_client()
        elif choice == "6":
            print("Exiting the system.")
            break
        else:
            print("Option Invalid, Try Again.\n")

if __name__ == "__main__":
    main()
