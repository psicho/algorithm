# Задача на программирование "кодирование Хаффмана".

r = input()
alf = [chr(i) for i in range(ord('a'),ord('z')+1)]
# r = list(r)
chastoty = {}
alfadict = []
for i in r:
    # print(chastoty[r.count(i)])
    if i not in alfadict:
        alfadict.append(i)
        if r.count(i) not in chastoty.keys():
            chastoty[r.count(i)] = list(i)
        elif r.count(i) in chastoty.keys():
            chastoty[r.count(i)].append(i)
# print(chastoty)
# print(chastoty.keys())
# print(chastoty.values())

k = ''
# print(len(k))
cod = {}

h = 0
# print(alf)

for i in reversed(range(len(r))):
    # print(i)
    if len(alfadict) == 1:
        # print(chastoty[len(r)][0])
        cod[chastoty[len(r)][0]] = '0'
    if i in chastoty:
        if len(r) == 1:
            print(chastoty[i][0])
            cod[chastoty['1'][0]] = '0'
        for u in range(len(chastoty[i])):
            for j in range(h):
                k += '1'
            if h != len(alfadict)-1:
                k += '0'
            cod[chastoty[i][u]] = k
            k = ''
            h += 1
# print('cod',cod)
k = ''
for i in r:
    k += cod[i]

print(len(cod), len(k))
t = ''
for i in cod:
    t += i+': '+ cod[i]
    print(t)
    t = ''
print(k)



