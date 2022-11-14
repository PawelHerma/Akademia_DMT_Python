def division(nom,denom):
    if denom == 0:
        print("Nieladnie tak dzielic przez 0")
        exit()
    help1 = nom // denom
    help = nom
    while nom != 0:
        help = nom * 10 % denom
        if help % denom == nom % denom:
            print(help1, "(", nom * 10 // denom ,")")
            break
        else:
            help1 += nom * 10 // denom / 10
            nom = nom * 10 % denom
            print(help1)


nom = int(input("Podaj licznik: "))
denom = int(input("Podaj mianownik: "))
division(nom,denom)