# Napisz funkcję wzor(x), posiadającą jeden argument. 
# Funkcja ma obliczać wartość wyrażenia:
#       3x^2-6x+1

def wzor(x):
    return 3 * (float(x) ** 2) - 6 * float(x) + 1

print("Funkcja 3x^2-6x+1")
x = float(input("Podaj argument x: "))
print("Wartość funkcji dla x równego " + str(x) + " wynosi: " + str(wzor(x)))