# program zgadnie wymyslona liczbe od 1 do 100
# program ma wbudowane sprawdzenie poprawnosci wprowadzanych danych
minimum = 1
maximum = 100
decision = "Nie"
while decision == "Nie":
    helper = " "
    print("Czy Twoja liczba to %(number)d (Tak/Nie): " % {"number": (maximum+minimum) // 2 })
    decision = input()
    if decision == "Tak":
        print("Tadaaaa")
        exit()
    while decision != "Nie" and decision != "Tak":
        print("Podano zly format odpowiedzi")
        decision = input()
    while helper != "Wieksza" and helper != "Mniejsza":
        helper = input("Czy Twoja liczba jest wieksza czy mniejsza? (Wieksza/Mniejsza): ")
        while helper != "Wieksza" and helper != "Mniejsza":
            print("Podano zly format odpowiedzi")
            helper = input()
    if helper == "Wieksza":
        minimum = (maximum + minimum) // 2
    else:
        maximum = (maximum + minimum) // 2