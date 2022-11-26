# Program prosi o podanie trzech liczb. 
# Jeżeli da się z nich zbudować trójkąt, to wyświetlana jest wartość obwodu trójkąta. 
# W przeciwnym wypadku wyświetlany jest komunikat “Nie istnieje trójkąt o podanych bokach”.

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

if a + b == c and b + c == a and c + a == b:
    print(a + b + c)

else:
    print("Nie istnieje trojkat o podanych bokach")