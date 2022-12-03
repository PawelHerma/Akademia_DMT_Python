# Dana jest lista liczb naturalnych [1,2,3,4,5,6,7,8,9,10,11,12].
# Program prosi użytkownika o podanie dowolnej liczby, 
# jeżeli podana przez użytkownika liczba znajduje się na liście, 
# to wyświetlamy komunikat “Liczba znajduje się na liście.” 
# w przeciwnym wypadku wyświetla się komunikat “Liczba nie jest na liście”.

lista = [1,2,3,4,5,6,7,8,9,10,11,12]
n = int(input("Podaj dowolną liczbę: "))
if n in lista:
    print("Liczba znajduje się na liście")
else:
    print("Liczba nie jest na liście")