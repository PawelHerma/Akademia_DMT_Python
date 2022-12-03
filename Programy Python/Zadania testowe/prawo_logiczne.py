#Sprawdź, czy podane wyrażenie jest prawem logicznym:

def checkA(p,q):
    return( not(p and q) or q )

p = [True, False]
q = [True, False]
checker = [0, 0, 0]

for i in range(2):
    for j in range(2):
        if checkA(p[i],q[j]):
            checker[0] += 1
        
for i in range(3):
    if checker[i] == 4:
        print("Wyrazenie A to prawo logiczne")
    else:
        print("Wyrazenie A to nie prawo logiczne")