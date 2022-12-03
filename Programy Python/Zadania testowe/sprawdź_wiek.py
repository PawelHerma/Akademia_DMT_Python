# Skrypt zapyta użytkownika o wiek. 
# Jeżeli użytkownik jest przed 18 wyświetli informację „Użytkownik niepełnoletni” 
# oraz zwróci ile lat zostało użytkownikowi do pełnoletności. 
# Użytkownikom pełnoletnim wyświetli informację „Użytkownik pełnoletni”. 
# Sprawdź czy wiek użytkownika nie przekracza 100 lat i wyświetla komunikat „200 lat”.

age = int(input("Podaj wiek: "))

if age >= 18:
    isMature = True
else:
    isMature = False

if isMature and age <= 100:
    print("Uzytkownik pelnoletni")
else:
    print("Uzytkownik niepelnoletni, brakuje " + str(18 - age) + " lat do pelnoletniosci")
