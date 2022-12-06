# Program prosi użytkownika o podanie dowolnej liczby. 
# Napisać funkcję checknumber, która sprawdza czy podane dane są liczbą, 
# jeżeli użytkownik nie poda liczby, to ekranie pojawia się napis 
# “To nie jest liczba. Spróbuj jeszcze raz”. 
# Program powinien domagać się podania liczby aż do skutku.

import re

def checknumber(user_input):
    regex = '^[\d]+$'
    while not re.match(regex, user_input):
        print("To nie jest liczba. Spróbuj jeszcze raz")
        user_input = input()
    return user_input


print(checknumber(input("Podaj liczbe: ")))