def gender(name):
    if name[-1] == "a":
        print("Jestes kobieta")
    else:
        print("Jestes mezczyzna")
name = input("Podaj swoje imie: ")
gender(name)