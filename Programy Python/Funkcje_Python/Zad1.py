def silnia(n):
    if n == 0 or n == 1:
        return 1
    else:
        wynik = n * silnia( n - 1 )
    return wynik

e = 1
n = input("Podaj liczbe: ")
n = int(n)

while( n > 0 ):
    e += 1 / silnia(n)
    n -= 1

print("Liczba Eulera: " + str(e))

# przy 17 Liczba Eulera robi się maksymalnie dokładna