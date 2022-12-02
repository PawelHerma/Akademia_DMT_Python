def fibonacci(n):
    if n == 0:
        exit()
    for i in range(n):
        if i == 0 or i == 1:
            return 1
        else:
            fibonacci(i) == fibonacci(i-1) + fibonacci(i-2)
        return fibonacci(n)

n = int(input("Podaj ile liczb ciagu chcesz: "))

tab = []

for i in range(n):
    tab.append(fibonacci(i+1))

print(tab)    