
# empty list initialized
inventory = []

# function to show all items in the inventory
def display_inventory():
    # checks if the inventory is empty
    if not inventory:  
        print("Inventory is empty.")
    else:
        # if inventory has items, prints each with index, nmame and quantity
        print("\nCurrent Inventory:")
        for idx, item in enumerate(inventory):
            print(f"{idx + 1}. {item['name']} - Quantity: {item['quantity']}")
            # prints a black for spacing
    print()

# function to add a new item in the inventory
def add_item():
    # takes in user input for item name and quantity
    name = input("Enter item name: ").strip()
    quantity = int(input("Enter quantity: "))
    for item in inventory:
        # loops through the inventory to check if the item already exists
        if item['name'].lower() == name.lower():
            item['quantity'] += quantity
            print(f"Updated quantity of {name}.")
            return
        # if the item does not exist, it appends the new item to the inventory
    inventory.append({'name': name, 'quantity': quantity})
    print(f"Added {name} to inventory.")

# function to update the quantity of an existing item
def update_item():
    name = input("Enter item name to update: ").strip()
    # loops through the inventory to find the item
    # searches for inventory matching item and updates the quantity
    for item in inventory:
        if item['name'].lower() == name.lower():
            new_qty = int(input("Enter new quantity: "))
            item['quantity'] = new_qty
            print(f"Updated {name}'s quantity to {new_qty}.")
            return
        # notification if not found
    print(f"{name} not found in inventory.")

# function to remove an item from the inventory
def remove_item():
    name = input("Enter item name to remove: ").strip()
    for item in inventory:
        # loops through the inventory to find the item
        if item['name'].lower() == name.lower():
            inventory.remove(item)
            print(f"Removed {name} from inventory.")
            return
    print(f"{name} not found in inventory.")
# function to display the menu and handle user input
def menu():
    # infinite loop for menu display
    while True:
        print("\n=== Inventory Management ===")
        print("1. View Inventory")
        print("2. Add Item")
        print("3. Update Item Quantity")
        print("4. Remove Item")
        print("5. Exit")

        choice = input("Choose an option: ")
# checks user input and calls the appropriate function
        if choice == '1':
            display_inventory()
        elif choice == '2':
            add_item()
        elif choice == '3':
            update_item()
        elif choice == '4':
            remove_item()
        elif choice == '5':
            print("Exiting Inventory System.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the system
menu()
