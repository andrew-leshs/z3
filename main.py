a = int(input())
mas = list()
for i in range(a):
    mas.append(input())

for i in mas:
    lis = i.split()
    summ = 0
    for j in lis:
        j = int(j)
        if j % 2 != 0:
            summ += j
    print(summ)
