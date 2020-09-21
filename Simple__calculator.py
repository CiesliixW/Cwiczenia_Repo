  
def is_number(string):
    try: 
        float(string)
        return float(string)
    except: 
        return None


def is_valid_operator(operator):
    if operator == "+" or "-" or "*" or "/":
        return True
    else:
        return False


def ask_for_a_number(force_valid_input):
    while force_valid_input == True:
        try: 
            user_input = float(input("Provide a number: "))
            return user_input
        except: 
            print("That didn't look like a number, try again!")
    if force_valid_input == False: 
        return None 
        

def ask_for_an_operator(force_valid_input):
    while force_valid_input == True:
        user_operator = input("Provide an operator one of *,-,/,+")
        if user_operator == "+" or "-" or "/" or "*":
            return user_operator 
    
    if force_valid_input == False:
        return None



def calc(operator, a, b):
    pass


def simple_calculator():
    pass


if __name__ == '__main__':
    simple_calculator()