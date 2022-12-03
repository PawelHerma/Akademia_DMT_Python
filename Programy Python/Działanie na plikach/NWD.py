#Program pyta uzytkownika o podanie pary liczb a i b. 
#Nastepnie zapisuje do pliku NWD.txt ich NWD w postaci NWD(a,b)=wynik.

import math

with open("NWD.txt","w") as file:

    a = int(input("Podaj pierwsza liczbe: "))
    b = int(input("Podaj druga liczbe: "))

    file.write(str("NWD(" + str(a) + "," + str(b) + ")=" + str(math.gcd(a,b))))
