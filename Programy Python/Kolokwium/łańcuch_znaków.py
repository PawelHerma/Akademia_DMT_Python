# Program prosi użytkownika o podanie łańcucha składającego się z 10 znaków.
# Jeżeli użytkownik poda właściwą długość łańcucha, 
# to na ekranie wyświetli się komunikat “Poprawna długość łańcucha” 
# w przeciwnym razie użytkownik zobaczy komunikat “Łańcuch ma niewłaściwą długość”. 
# Sprawdzanie długości ciągu ma się odbyć tylko raz.

lancuch = input("Podaj lancuch znakow: ")
if len(lancuch) == 10:
    print("Poprawna długość łańcucha")
else:
    print("Łańcuch ma niewłaściwą długość")