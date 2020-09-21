import os

def add(x,y):
    return x + y

def substract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x/y



cos = "y"
while cos == "y":
    print("\nWelcome in Calculator! Enter your equation. Press enter after each number or operator.")
    number1 = input("")
    op = input("")
    number2 = input("")

    if op == "+": 
        try: 
            add_result = add(float(number1), float(number2))
            print(f"The result is {add_result}\n")
            cos = input("Do you want to execute another operation? y/n: ") 
        except: 
            print("\nINVALID INPUT!")
            cos = input("Do you want to try again? y/n: ")

        

    elif op == "-": 
        try: 
            add_result = substract(float(number1), float(number2))
            print(f"The result is {add_result}\n")
            cos = input("Do you want to execute another operation? y/n: ")
        except: 
            print("\nINVALID INPUT!")
            cos = input("Do you want to try again? y/n: ")

    elif op == "*": 
        try: 
            add_result = multiply(float(number1), float(number2))
            print(f"The result is {add_result}\n")
            cos = input("Do you want to execute another operation? y/n: ")
        except: 
            print("\nINVALID INPUT!")
            cos = input("Do you want to try again? y/n: ")

    elif op == "/": 
        try: 
            add_result = multiply(float(number1), float(number2))
            print(f"The result is {add_result}\n")
            cos = input("Do you want to execute another operation? y/n: ")
        except: 
            print("\nINVALID INPUT!")
            cos = input("Do you want to try again? y/n: ")
    
    else:
        print("Invalid Input")
        cos = input("Do you want to try provide valid input? y/n: ")
        if cos =="n":
            print("Thanks for using calculator. End of the program")
            quit()


            
        