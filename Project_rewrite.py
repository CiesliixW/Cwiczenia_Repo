def min(x, y):
    if x > y: 
        return y
    elif x < y: 
        return x
    else: 
        return "Remis"

def max(x, y):
    try:

        if int(x) > int(y): 
            return x
        elif x < y: 
            return y
        else: 
            return "Remis"

    except: 
        return "Wprowadzono złe dane"


wieksza = max("a", "b")
print(wieksza)

