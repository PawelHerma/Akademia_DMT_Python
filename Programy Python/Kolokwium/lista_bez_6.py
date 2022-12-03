# Napisz program, 
# który stworzy listę składającą się z liczb naturalnych od 1 do 500, 
# ale bez liczb podzielnych przez 6.

lista = []
for i in range(1,501):
    if i % 6 != 0:
        lista.append(i)
# sprawdzenie listy: 
# print(lista)