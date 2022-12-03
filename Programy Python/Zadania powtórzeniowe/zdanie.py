# Wczytać od użytkownika zdanie typu str(), następnie:
#   a zliczyć wyrazy w zdaniu,
#   b liczyć liczbę wszystkich liter.

zdanie = input("Podaj swoje zdanie \n")
wyrazy = 1
litery = 0
for i in range(len(zdanie)):
    if zdanie[i] == " ":
        wyrazy += 1
    else:
        litery += 1
print("Twoje zdanie zawiera:\n - wyrazy:",wyrazy,"\n - litery:",litery)