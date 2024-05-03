# The Calculator App
# Task 1: Create functions for each arithmetic operation.

def calculator_func(operation, num_1, num_2):
    
    if operation == "addition":
        return num_1 + num_2
    if operation == "subtraction":
        return num_1 - num_2
    if operation == "multiplication":
        return num_1 * num_2
# The Calculator App
# Task 3: Ensure your program can handle division by zero and other potential errors
    if operation == "division":
        if num_1 == 0 or num_2 == 0:
            return 0
        else:
            return num_1 / num_2
# The Calculator App
# Task 2: Implement user input to receive numbers and an operation choice.

operation = (input("Please enter one of these operations: addition, subtraction, multiplication, division: "))
num_1 = int(input("Please enter a number: "))
num_2 = int(input("Please enter another number: "))

result = calculator_func(operation, num_1, num_2)

print(calculator_func(operation, num_1, num_2))




# The Shopping List Maker
# Task 1: Write a function that lets the user add items to a list.

cart = []
def shopping_list_func(user_selection, add_item, remove_item):
    
    while True:
        
        if user_selection == "add":
            add_item = input("What item would you like to add to your cart? ")
            cart.append(user_selection)
            print(f"{user_selection} was added to your cart!")
            break
# The Shopping List Maker
# Task 2: Include a feature to remove items from the list.
        elif user_selection == "remove":
            remove_item = input("What item would you like to remove from your cart?")
            if remove_item in cart:
                cart.remove(remove_item)
                print(f"{remove_item} was removed from your cart!")
            else:
                print(f"{remove_item} was not in your cart.")
# The Shopping List Maker
# Task 3: Add a function that prints out the entire list in a formatted way.      
        else:
            print(f"Thanks for shopping with us. These are the items you are purchasing today: {cart}.")        

user_selection = input("Let's shop! Please select from these options: 'add' to add an item, 'remove' to remove an item or 'done' to end adding items to your cart: ")
add_item = input("What item would you like to add to your cart? ")
remove_item = input("What item would you like to remove from your cart?")        
        
final_cart = shopping_list_func(user_selection, add_item, remove_item)

print(shopping_list_func(user_selection, add_item, remove_item))