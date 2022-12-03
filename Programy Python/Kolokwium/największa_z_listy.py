# Dana jest lista [-3,0,56,12,-23,45,10,8]
# Napisz program, który wyświetli na ekranie największą liczbę z podanej listy.

lista = [-3,0,56,12,-23,45,10,8]
for i in range(len(lista)):
    for j in range(len(lista)):
        if lista[i] > lista[j]:
            pomoc = lista[j]
            lista[j]=lista[i]
            lista[i]=pomoc
# pierwszy element listy staje się największy
# sprawdzenie: print(lista)
print(lista[0])