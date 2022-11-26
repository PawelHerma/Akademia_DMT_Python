# Wypisz na ekranie imiona pięciu członków rodziny.
# a. Użyj tylko jednej instrukcji print i wypisz je w jednym wierszu
#       Wiola, Ewa, Kasia, Tomek, Rafał
# b. Użyj tylko jednej instrukcji print i wypisz je w osobnych wierszach
#       Wiola
#       Ewa
#       Kasia
#       Tomek
#       Rafał
# c. Użyj osobnych instrukcji print dla każdego słowa i wypisz je w jednym wierszu
#       Wiola, Ewa, Kasia, Tomek, Rafał
# d. Użyj osobnych instrukcji print dla każdego słowa i wypisz je w osobnych wierszach
#       Wiola
#       Ewa
#       Kasia
#       Tomek
#       Rafał

imiona = ["Wiola","Ewa","Kasia","Tomek","Rafal"]

# AD a.
print(", ".join(imiona))
print(imiona[0],",",imiona[1],",",imiona[2],",",imiona[3],",",imiona[4])

# AD b.
for i in range(5):
    print(imiona[i])

# AD c.
print(imiona[0], end=", ")
print(imiona[1], end=", ")
print(imiona[2], end=", ")
print(imiona[3], end=", ")
print(imiona[4])

# AD 4
print(imiona[0])
print(imiona[1])
print(imiona[2])
print(imiona[3])
print(imiona[4])