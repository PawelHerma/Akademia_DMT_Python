# Utwórz plik kolokwium.txt w którym umieścisz numery zadań z tego kolokwium 
# z dopiskiem zad. Napisy powinny znajdować się jeden pod drugim.

with open("kolokwium.txt","w") as plik:
    for i in range(1,12):
        tekst = "zad." + str(i)
        plik.write(tekst + "\n")
