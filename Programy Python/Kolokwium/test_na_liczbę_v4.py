# Program prosi użytkownika o podanie dowolnej liczby. 
# Napisać funkcję checknumber, która sprawdza czy podane dane są liczbą, 
# jeżeli użytkownik nie poda liczby, to ekranie pojawia się napis 
# “To nie jest liczba. Spróbuj jeszcze raz”. 
# Program powinien domagać się podania liczby aż do skutku.

import re

regex = '\d'

def checknumber():
    dane = input("Podaj liczbe: ")

    if re.search(regex,dane):
        print("Twoja liczba to" , dane)
        exit()
    else:
        print("To nie jest liczba. Spróbuj jeszcze raz")
        checknumber()

checknumber()