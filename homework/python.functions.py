# The Calculator App
# Task 1: Create functions for each arithmetic operation.
# The Calculator App
# Task 2: Implement user input to receive numbers and an operation choice.

def calculator_func():
    operation = (input("Please enter one of these operations: addition, subtraction, multiplication, division: "))
    
    if operation == "addition":
        num_1 = int(input("Please enter a number: "))
        num_2 = int(input("Please enter another number: "))
        return num_1 + num_2
    elif operation == "subtraction":
        num_1 = int(input("Please enter a number: "))
        num_2 = int(input("Please enter another number: "))
        return num_1 - num_2
    elif operation == "multiplication":
        num_1 = int(input("Please enter a number: "))
        num_2 = int(input("Please enter another number: "))
        return num_1 * num_2
# The Calculator App
# Task 3: Ensure your program can handle division by zero and other potential errors
    elif operation == "division":
        num_1 = int(input("Please enter a number: "))
        num_2 = int(input("Please enter another number: "))
        if num_1 == 0 or num_2 == 0:
            return 0
        else:
            return num_1 / num_2
    else:
        return "Please enter valid response"

print(calculator_func())




# The Shopping List Maker
# Task 1: Write a function that lets the user add items to a list.

cart = []
def shopping_list_func():
    
    while True:
        user_selection = input("Let's shop! Please select from these options: 'add' to add an item, 'remove' to remove an item or 'done' to end adding items to your cart: ")
        if user_selection == "add":
            add_item = input("What item would you like to add to your cart? ")
            cart.append(add_item)
            print(f"{add_item} was added to your cart!")

# The Shopping List Maker
# Task 2: Include a feature to remove items from the list.
        elif user_selection == "remove":
            remove_item = input("What item would you like to remove from your cart?")
            if remove_item in cart:
                cart.remove(remove_item)
                print(f"{remove_item} was removed from your cart!")
            elif remove_item not in cart:
                print(f"{remove_item} was not in your cart.")
            else:
                print(user_selection)
# The Shopping List Maker
# Task 3: Add a function that prints out the entire list in a formatted way.      
        elif user_selection == "done":
            print(f"Thanks for shopping with us. These are the items you are purchasing today: {cart}.")    
        else:
            print(user_selection)    

shopping_list_func()