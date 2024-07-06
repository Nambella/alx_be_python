def display_menu():
    print("Shopping List Manager")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the list")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            pass
        elif choice == '2':
            # Prompt for and remove an item
            pass
        elif choice == '3':
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

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

if __name__ == "__main__":
    main()
