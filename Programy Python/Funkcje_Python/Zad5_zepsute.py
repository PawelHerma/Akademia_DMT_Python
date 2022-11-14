def division(nom,denom):
    if denom == 0:
        print("Nieladnie tak dzielic przez 0")
        exit()
    if nom / denom == (nom / denom) * 10 - (nom * 10 // denom): #nie działa, nie mam pomysłu na to :/
        print(nom//denom,".(",nom%denom*denom,")")
    else:
        print(nom/denom)

nom = int(input("Podaj licznik: "))
denom = int(input("Podaj mianownik: "))
division(nom,denom)