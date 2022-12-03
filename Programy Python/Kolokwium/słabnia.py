# slabnia - suma kolejnych liczb az do n

n = int(input("Podaj n: "))
slabnia = 0
for i in range(n):
    slabnia += i+1
print(str(n)+"?="+str(slabnia))