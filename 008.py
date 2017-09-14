# Задача на программирование "декодирование Хаффмана".

r = str(input()).split(' ')
# print(r)
dis = {}
for i in range(int(r[0])):
    t = str(input()).split(': ')
    dis[t[1]] = t[0]
s = list(input())

l = ''
o = ''
for i in s:
    l += i
    # print('l',l)
    if l in dis:
        o += dis[l]
        l = ''
print(o)