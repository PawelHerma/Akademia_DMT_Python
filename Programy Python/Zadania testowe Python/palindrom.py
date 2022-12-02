# sprawdza czy wpisany tekst jest palindromem
tekst = input("Podaj tekst do sprawdzenia: ")
tekst = tekst.replace(" ","") # dzieki temu dziala ze zdaniami w stylu "kobyla ma maly bok"
for i in range(len(tekst)):
    if tekst[i] != tekst[len(tekst) - i - 1]:
        print("To nie jest palindrom")
        exit()
print("Jest palindromem")