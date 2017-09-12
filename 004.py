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
# print(l)
f.append(l[0][1])
l.pop(0)
# print(f)
t = len(l)
if len(l):
    # for i in range(t):
    while len(l):
        # print('l2',l)
        # print('f2',f)
        if int(l[0][0]) <= int(f[-1]) and int(l[0][1]) >= int(f[-1]):
            l.pop(0)
            # print(len(l))
        else:
            f.append(l[0][1])
            l.pop(0)
        if not len(l):
            break
print(len(f))
for i in f:
    print(i)



