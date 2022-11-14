# wylicza NWD dla n liczb całkowitych
def nwda(a, b):
    while b != 0:
        c = int(a) % int(b)
        a = b
        b = c
    return a

def nwdb(l, n):
    nwdv = l[0]
    for i in range(int(n)):
        nwdv = nwda(nwdv, l[i])
    return nwdv

n = int(input("Podaj dla ilu liczb chcesz znalezc NWD: "))
tab = [0] * n
for i in range(n):
    print("Podaj %(num)d liczbe: " % {"num": i+1})
    tab[i] = input()
fin = nwdb(list(tab), n)
print(fin)