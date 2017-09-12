# Задача на программирование "непрерывный рюкзак".

r = list(str(input()).split(' '))
l = []
f = []
for i in range(int(r[0])):
    k = list(str(input()).split(' '))
    if not l:
        l.append(k)
        continue
    for j in range(len(l)):
        if int(l[j][0]) / int(l[j][1]) < int(k[0]) / int(k[1]):
            l.insert(j, k)
            break
        if j == len(l) - 1:
            l.append(k)
print(l)
v = float(r[1])
cost = 0
for i in range(len(l)):
    if float(l[i][1]) == v:
        cost += float(l[i][0])
        break
    if float(l[i][1]) < float(v):
        v -= float(l[i][1])
        cost += float(l[i][0])
        # print(v, cost)
    else:
        cost += round(float(l[i][0],3)/float(l[i][1],3)*float(v,3),3)
        break
    pass
print('%.3f' %cost)

