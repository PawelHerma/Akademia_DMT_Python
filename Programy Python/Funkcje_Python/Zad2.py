dochod = int(input("Podaj dochod: "))
podatek = int(input("Ile wynosi % podatku: "))
przychod = dochod * ((100 - podatek) / 100)
print("Twój przychod wynosi: " + str(przychod))