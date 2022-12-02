# isArmstrong sprawdza czy podana liczba jest liczbą Armstronga
def isArmstrong(n):
    s = str(n)
    n = int(n)
    h = n
    tab = [0] * len(s)
    i = 0
    while n >= 10:
        tab[len(s)-1-i] = n % 10
        n = n // 10
        i += 1
    tab[0] = n
    arm = 0
    for i in range(len(s)):
        arm += tab[i]**len(s)
    if arm == h:
        return True
    else:
        return False

num = input("Podaj liczbe do sprawdzenia: ")
num = int(num)
if isArmstrong(num) == True:
    print("Jest liczba Armstronga")
else:
    print("Nie jest liczba Armstronga")