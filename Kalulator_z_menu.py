import os

def add(x,y):
    return x + y

def substract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x/y

def is_number(x,y):

    try:
        float(x,y)
        return True
    except:
        return False

cos = "y"
while cos == "y":
    
    print("\n **MENU**")
    print("\n(1) Add")
    print("(2) Substract")
    print("(3) Multiply")
    print("(4) Divide\n")

    option = input("Provide operation to execute (1/2/3/4): ")
    print("")


    if option == "1":
        number1 = (input("Provide first number: "))
        number2 = (input("Provide second number: "))
        
        try: 
            add_result = add(float(number1), float(number2))
            print(f"The result is {add_result}\n")
            cos = input("Do you want to execute another operation? y/n: ")
        except: 
            print("\nINVALID INPUT!")
            cos = input("Do you want to try again? y/n: ")
            
        os.system("cls || clear")

    elif option == "2":
        number1 = float(input("Provide first number: "))
        number2 = float(input("Provide second number: "))
        sub_result = substract(number1, number2)
        print(f"The Result is {sub_result}\n")
        cos = input("Do you want to execute another operation? y/n: ")

    elif option == "3":
        number1 = float(input("Provide first number: "))
        number2 = float(input("Provide second number: "))
        mul_result = multiply(number1, number2)
        print(f"The Result is {mul_result}\n")
        cos = input("Do you want to execute another operation? y/n: ")

    elif option == "4":
        number1 = float(input("Provide first number: "))
        number2 = float(input("Provide second number: "))
        dev_result = divide(number1, number2)
        print(f"The result is {dev_result}\n")
        cos = input("Do you want to execute another operation? y/n: ")
    else:
        print("Invalid Input")
        cos = input("Do you want to try provide valid input? y/n: ")
        if cos =="n":
            print("Thanks for using calculator. End of the program")
            quit()

    if cos == "n": 
        print("\nThanks for using calculator. End of the program\n")
        quit()


