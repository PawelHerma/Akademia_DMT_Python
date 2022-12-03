# Program prosi użytkownika o podanie dowolnej liczby. 
# Napisać funkcję checknumber, która sprawdza czy podane dane są liczbą, 
# jeżeli użytkownik nie poda liczby, to ekranie pojawia się napis 
# “To nie jest liczba. Spróbuj jeszcze raz”. 
# Program powinien domagać się podania liczby aż do skutku.

def checknumber():
    dane = input("Podaj liczbe: ")

    for i in range( len( dane ) ):

        if str( dane[i] ) != str( ord( dane[i] ) - 48):
            
            print("To nie jest liczba. Spróbuj jeszcze raz")
            checknumber()

    print("Twoja liczba to" , dane)
    exit()

checknumber()