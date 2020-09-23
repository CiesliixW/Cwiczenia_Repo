  
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
        try: 
            user_input = float(input("Provide a number: "))
            return user_input
        except: 
            return None 
        

def ask_for_an_operator(force_valid_input):
    while force_valid_input == True:
        user_operator = input("Provide an operator: ")
        if user_operator == "+" or "-" or "/" or "*":
            return user_operator
        else: 
            print("Invalid operator, try again!")
    
    if force_valid_input == False:
        user_operator = input("Provide an operator: ")
        if user_operator == "+" or "-" or "/" or "*":
            return user_operator
        else: 
            return None



def calc(operator, a, b):
    if not is_valid_operator(operator) or not is_number(a) or not is_number(b):
        return None
    
    result = None
    if operator == "+":
        result = a + b
        return result 
    elif operator == "-":
        result == a - b 
        return result
    elif operator == "/":
        if b == 0:
            print("Error, nie można dzielic przez 0")
            return None
        else:
            result = a / b
            return result
    elif operator == "*":
        result = a * b
        return result


        

def simple_calculator():
    while True: 
        a = ask_for_a_number(force_valid_input=False)
        if not a:
            break 
        
        op = ask_for_an_operator(force_valid_input=True)

        b = ask_for_a_number(force_valid_input = True)

        result = calc(op, a, b)
 
        print(result)

if __name__ == '__main__':
    simple_calculator()