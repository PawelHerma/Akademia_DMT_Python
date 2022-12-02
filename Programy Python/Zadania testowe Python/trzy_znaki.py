goodData = False

def correct(a,b,c):

    if type(a) == type(b) and type(b) == type(c) and type(a) is int:
        print("Podano poprawnie trzy liczby")
        goodData = True

    elif type(a) == type(b) and type(b) == type(c) and type(a) is str:
        print("Poprawnie wprowadzono dane")
        goodData = True
    
    else:
        print("Dane zostały wprowadzone blednie, wprowadz je ponownie")
        goodData = False
    
    if goodData == True:
        exit()
    
    else:
        a = input("Podaj a: ")
        b = input("Podaj b: ")
        c = input("Podaj c: ")
        correct(ifDigit(a),ifDigit(b),ifDigit(c))

def ifDigit(n):
    try:
        n = int(n)
    
    except ValueError:
        
        try:
            n = str(n)
        
        except ValueError:
            print(n," nie jest ani liczba ani tekstem")
    
    return n

a1 = input("Podaj a: ")
b1 = input("Podaj b: ")
c1 = input("Podaj c: ")

goodData = False

correct(ifDigit(a1),ifDigit(b1),ifDigit(c1))