def display_menu():
    print("\nMenu:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the list")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter the item name: ")
    shopping_list.append(item)
    print(f"{item} added to the list.")

def remove_item(shopping_list):
    item = input("Enter the item name to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the list.")
    else:
        print(f"{item} not found in the list.")

def view_list(shopping_list):
    print("\nCurrent Shopping List:")
    for item in shopping_list:
        print(item)

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Exiting. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            
if __name__ == "__main__":
    main()