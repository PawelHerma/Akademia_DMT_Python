# sortowanie babelkowe
def bubbleSort(tab):
    n = len(tab)
    help1 = n
    while n > 1:
        for i in range(int(help1)-1):
            if tab[i] > tab[i+1]:
                help2 = tab[i+1]
                tab[i+1] = tab[i]
                tab[i] = help2
        n -= 1
    return tab

n = int(input("Ile liczb chcesz posortowac: "))
tab = [None] * n
for i in range(n):
    print("Podaj %(num)d liczbe: " % {"num": i+1})
    tab[i] = input()
print("Posortowano")
print(bubbleSort(tab))