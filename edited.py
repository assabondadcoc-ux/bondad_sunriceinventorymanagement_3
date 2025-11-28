inventory = []

while True:
    print("\nSunRice Inventory Management System")
    print("+----+------------------------------------+")
    print("| No |              Action                |")
    print("+----+------------------------------------+")
    print("| 1  | Add Rice Type, Quantity & Reorder  |")
    print("| 2  | Update Rice Information            |")
    print("| 3  | Delete Rice Type                   |")
    print("| 4  | Search Rice Type                   |")
    print("| 5  | View All Rice Stocks               |")
    print("| 6  | Exit                               |")
    print("+----+------------------------------------+")

    choice = input("Select an option (1-6): ")

   
    if choice == '1':
        rice_types = []

       
        while True:
            name = input("Enter rice type (or type 'no' to stop): ")

            if name.lower() == "no":
                if not rice_types:
                    print("You did not enter any rice type.")
                else:
                    print("\nStopped adding rice types.")
                    print("\n")
                  
                break

            is_duplicate = False
            for item in inventory:
                if item[0].lower() == name.lower():
                    print(f"Error: '{name}' already exists in the inventory.")
                    is_duplicate = True
                    break
            
            if is_duplicate:
                continue
            if name in rice_types:
                print(f"Error: '{name}' is already listed in this current batch to be added.")
                continue

            rice_types.append(name)

        if not rice_types:
            continue

      
        quantities = {}
        for name in rice_types:
            quantity = 0
            while quantity <= 0:
                q = input(f"Enter quantity for '{name}' (in sacks): ")
                if q.isdigit():
                    quantity = int(q)
                    if quantity <= 0:
                        print("Please enter a positive number.")
                else:
                    print("Invalid input. Please enter a number.")
            quantities[name] = quantity

       
        reorders = {}
        for name in rice_types:
            reorder = 0
            while reorder <= 0:
                r = input(f"Enter reorder level for '{name}' (in sacks): ")
                if r.isdigit():
                    reorder = int(r)
                    if reorder <= 0:
                        print("Please enter a positive number.")
                else:
                    print("Invalid input. Please enter a number.")
            reorders[name] = reorder

       
        for name in rice_types:
            inventory.append([name, quantities[name], reorders[name]])

        print("\n============================================")
        print("Added the following rice types:")
        for name in rice_types:
            print(f" - {name}: {quantities[name]} sacks (Reorder level: {reorders[name]})")
        print("============================================")

   
    elif choice == '2':
        if not inventory:
            print("No rice types in inventory.")
        else:
            print("\nCurrent Rice Inventory:")
            print("+------------------+----------------+----------------------+")
            print("| Rice Type        | Quantity       | Reorder Level        |")
            print("+------------------+----------------+----------------------+")
            for item in inventory:
                print(f"| {item[0]:<16} | {item[1]:<14} | {item[2]:<20} |")
            print("+------------------+----------------+----------------------+")

            name = input("Enter rice type to update: ")
            found = False

            for item in inventory:
                if item[0] == name:
                    found = True

                    new_quantity = 0
                    while new_quantity <= 0:
                        q = input("Enter new quantity in sacks: ")
                        if q.isdigit():
                            new_quantity = int(q)
                            if new_quantity <= 0:
                                print("Please enter a positive number.")
                        else:
                            print("Invalid input. Please enter a number.")

                    new_reorder = 0
                    while new_reorder <= 0:
                        r = input("Enter new reorder level in sacks: ")
                        if r.isdigit():
                            new_reorder = int(r)
                            if new_reorder <= 0:
                                print("Please enter a positive number.")
                        else:
                            print("Invalid input. Please enter a number.")

                    item[1] = new_quantity
                    item[2] = new_reorder

                    print("\n============================================")
                    print(f"'{name}' information updated successfully!")
                    print("============================================")
                    break

            if not found:
                print("Rice type not found.")

    
    elif choice == '3':
        if not inventory:
            print("No rice types to delete.")
        else:
            print("\nCurrent Rice Inventory:")
            print("+------------------+----------------+--")
            print("+------------------+----------------+--")
            name = input("Enter rice type to delete: ")
            for item in inventory:
                if item[0] == name:
                    inventory.remove(item)
                    print(f"¸ Deleted '{name}'.")
                    break
            else:
                print("Rice type not found.")
 
    elif choice == '4':
        name = input("Enter rice type to search: ")
        for item in inventory:
            if item[0] == name:
                print(f"Found: {item[0]} - Quantity: {item[1]} sacks, Reorder Level: {item[2]} sacks")
                break
        else:
            print("Product not found.")
 
    elif choice == '5':
        if not inventory:
            print("No products in inventory.")
        else:
            print("\nInventory Report:")
            print("+------------------+----------------+----------------------+")
            print("| Rice Type        | Quantity       | Reorder Level        |")
            print("+------------------+----------------+----------------------+")
            for item in inventory:
                print(f"| {item[0]:<16} | {item[1]:<14} | {item[2]:<20} |")
            print("+------------------+----------------+----------------------+")
 
    elif choice == '6':
        print(" Exiting the Inventory Management System.")
        break
 
    else:
        print("Invalid choice. Please try again.")