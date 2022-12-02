# Napisz program, który prosi o podanie liczby naturalnej,
# a następnie wypisuje z ilu cyfr składa się wpisana wartość, 
# a także informację o sumie tworzących ją cyfr.
# Dla uproszczenia załóż, że podana liczba jest poprawna (czyli rzeczywiście naturalna).

n = input("Podaj liczbe naturalna: ")
print("Liczba składa się z",len(n),"liczb")
sum = 0
for i in range(len(n)):
    sum += int(n[i])
print("Suma jego cyfr wynosi:",sum)