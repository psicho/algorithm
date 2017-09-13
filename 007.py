# Задача на программирование "кодирование Хаффмана".

r = input()
alf = [chr(i) for i in range(ord('a'),ord('z')+1)]
bu = 'a'
for i in r:
    if ord(i) > ord(bu):
        bu = i
# print(bu)

k = ''
cod = {}
h = 0
# print(alf)
for i in range(len(alf)):
    if r.count(alf[i]) > 0:
        for j in range(len(cod)):
            k += '1'
        if bu != alf[i]:
            k += '0'
        cod[alf[i]] = k
        k = ''
        if len(r) == 1:
            cod[alf[i]] = '0'

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



