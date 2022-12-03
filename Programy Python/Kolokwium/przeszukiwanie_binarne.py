# Używając algorytmu przeszukiwania binarnego rozwiązać równanie:
# x^2=2
# z dokładnością do 0,0001.

epsilon = 0.0001
maximum = 2.0
minimum = 1.0
while (maximum - minimum) > epsilon:
    epsilon = 0.0001
    srednia = (maximum + minimum)/2
    if srednia ** 2 < 2:
        pomoc = (maximum + minimum)/2
        minimum = pomoc
    elif srednia ** 2 > 2:
        pomoc = (maximum + minimum)/2
        maximum = pomoc
print((minimum+maximum)/2)
