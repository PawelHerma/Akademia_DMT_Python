# Napisz program, 
# który wypisze pierwsze N liczb naturalnych w kolejności 
# rosnącej i malejącej w osobnych kolumnach

n = int(input("Podaj n: "))

for i in range(n+1):
    print(i,n-i)