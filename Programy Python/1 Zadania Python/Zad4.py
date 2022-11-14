# isPrime sprawdza czy podana liczba jest pierwsza
def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    mid = int(n**0.5) + 1
    for div in range(3, mid, 2):
        if n % div == 0:
            return False
    return True
# program wypisuje 40 pierwszych liczb pierwszych
i = 1
s = 1
while s <= 40:
    if isPrime(i) == True:
        print(i)
        s += 1
        i += 1
    else:
        i += 1