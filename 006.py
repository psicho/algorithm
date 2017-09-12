# Задача на программирование "различные слагаемые".

r = int(input())
sum = 0
slog = []
stre = ''
for i in range(1,r+1):
    if r == 1:
        slog.append(1)
        break
    if r == 2:
        slog.append(2)
        break
    sum += int(i)
    slog.append(i)
    # print('sum',sum)
    # print('slog',slog)
    if sum == r:
        break
    if sum > r:
        sum -= int(slog.pop())
        sum -= int(slog.pop())
        i -= 1
        # print('sum', sum)
        while sum < r:
            i += 1
            if sum + int(i) == r:
                sum += int(i)
                slog.append(i)
                break
        if sum == r:
            break
    # print(slog)
for i in slog:
    stre += str(i) + ' '
print(len(slog))
print(stre)


