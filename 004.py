# Задача на программирование "покрыть отрезки точками".

r = int(input())
l = []
f = 0
for i in range(r):
    k = list(str(input()).split(' '))
    if not l:
        l.append(k)
        continue
    for j in range(len(l)):
        if int(l[j][1]) > int(k[1]):
            l.insert(j, k)
            break
        if j == len(l) - 1:
            l.append(k)
for i in range(len(l)):

print(l)


