import os

Exit_word = "quit"

def menu():
    print("(1) Addition")
    print("(2) Substraction")
    print("(3) Multiplication")
    print("(4) Division \n")
    print(f"Type: \"{Exit_word}\" to end the program")


def addition():
    addition_input1 = input("Provide first number: ")
    addition_input2 = input("Provide second number: ")
    addition_result = int(addition_input1) + int(addition_input2)
    print(f"{addition_input1} + {addition_input2} = {addition_result}")
    input("Press enter to continue")
    
    

def substraction():
    substraction_input1 = input("Provide minued: ")
    substraction_input2 = input("Provide subtrahend: ")
    substraction_result = int(substraction_input1) - int(substraction_input2)
    print(f"{substraction_input1} - {substraction_input2} = {substraction_result}")
    input("Press enter to continue")

def multiplication(): 
    multiplication_input1 = input("Provide first factor: ")
    multiplication_input2 = input("Provide second factor: ")
    multiplication_result = int(multiplication_input1) *  int(multiplication_input2)
    print(f"{multiplication_input1} * {multiplication_input2} = {multiplication_result}")
    input("Press enter to continue")

should_continue = True 
while should_continue:
    
    os.system("cls || clear")
    menu()
    option = input("Provide desired action's number (1/2/3): ")

    if option == Exit_word:
        should_continue = False
        
    if option == "1":
        addition()

    if option == "2":
        substraction()
    
    if option == "3":
        multiplication()

print("End of program")
    
