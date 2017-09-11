# Задача на программирование "покрыть отрезки точками".

r = int(input())
l = []
f = []
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
f.append(l.pop(0))
print(l[0])
print(f)
print(f[-1])
while len(l) > 0:
    if int(l[0][0]) <= int(f[-1][1]) and int(l[i][1]) >= int(f[i-1][1]):
        l.pop(0)
    else:
        f.append(l.pop(0))
    print(l)
    print(f)



