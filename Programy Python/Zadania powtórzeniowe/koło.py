# Napisz program, który oblicza pole i obwód koła o promieniu podanym przez użytkownika. 
# Wartość stałej π weź z biblioteki math. 
# Promień nie może być ujemny. 
# W przypadku podania liczby ujemnej, program powinien wypisywać 
# komunikat informujący o błędnej wartości i nic nie liczyć.

from math import pi

r = int(input("Podaj promien kola: "))
obwod = 2 * pi * r
pole = pi * (r**2)
print("Obwod kola o promieniu",r,"wynosi",obwod,"a pole",pole)