"""
Program:
    - poprawnosc numeru PESEL (liczba kontrolna)
    - podaje plec wlasciciela
    - podaje wiek wg rocznika
Uwaga: jeśli liczba kontrolna numeru PESEL
    będzie nieprawidłowa, program zakończy swoje działanie
"""
def isValid(pesel):
    valid = 0
    for i in range(len(pesel)-1):
        if i % 4 == 0:
            valid += (pesel[i]*1) % 10
        elif i % 4 == 1:
            valid += (pesel[i]*3) % 10
        elif i % 4 == 2:
            valid += (pesel[i]*7) % 10
        elif i % 4 == 3:
            valid += (pesel[i]*9) % 10
    valid = 10 - (valid % 10)
    if valid == pesel[10]:
        return True
    else:
        return False

def gender(pesel):
    if pesel[9] % 2 == 0:
        return "Kobieta"
    else:
        return "Mezczyzna"

def age(pesel):
    year = int(str(pesel[0]) + str(pesel[1]))
    if year > 22:
        return 122 - year
    else:
        return 22 - year

peselStr = str(input("Podaj PESEL: "))
peselList = [0] * len(peselStr)
for i in range(len(peselStr)):
    peselList[i] = int(peselStr[i])
if isValid(peselList) == True:
    print("PESEL jest prawdziwy")
else:
    print("PESEL nie jest prawdziwy")
    exit()
print("Plec wlasciciela: %(gender)s " %  {"gender": gender(peselList)})
print("Wlasciciel ma %(age)d lat" % {"age": age(peselList)})