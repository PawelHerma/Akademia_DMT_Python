# Działanie programu powinno być zbliżone do następującego:
# Użytkownik wybiera czy obstawia resztę, czy orła (literka r – reszka, literka o – orzeł)
# Po dokonaniu wyboru, Komputer odlicza 3,2,1, a następnie dokonuje 'rzutu’, czyli losowego wyboru orzeł / reszka.
# Komputer wyświetla wynik rzutu.
# Jeżeli wygrał użytkownik, to dodaje punkt dla użytkownika, jeżeli komputer to dodaje punkt dla komputera.
# Wyświetla wyniki
# Wracamy do punktu 1.

from time import sleep
from random import choice
ja = 0
gracz = 0
wybor = "1"
while wybor != "0":
    wybor = input("orzel(o) czy reszka(r)")
    rzut = choice(["o","r"])
    if wybor == "0":
        break
    elif wybor == rzut:
        print("Wygrales!")
        gracz += 1
    else:
        print("wygralem!")
        ja += 1
    print("Tablica wynikow:\n Ja:",ja,"\n Ty:",gracz)
exit()