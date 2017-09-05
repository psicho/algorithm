def fib_digit(n):
    f1 = 0
    f2 = 1
    if n == 0:
        return f1
    if n == 1:
        return f2

    for i in range(n - 1):
        f = f1 + f2
        if f > 9:
            f = f % 10
        f1 = f2
        f2 = f
    return f

print(fib_digit(875577))