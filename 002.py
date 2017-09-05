# Задача на программирование повышенной сложности: огромное число Фибоначчи по модулю
# Даны целые числа 1≤n≤10^18 и 2≤m≤10^5, необходимо найти остаток от деления n-го числа Фибоначчи на m.

def fib_mod(n, m):
    def fib_digit(n): # берём функция нахождения последней цифры n-го числа Фибоначи из предыдущей задачи 001.
        f1 = 0
        f2 = 1
        if n == 0:
            return f1
        if n == 1:
            return f2

        for i in range(n-1):
            f = f1 + f2
            if f > 9:
                f = f%10
            f1 = f2
            f2 = f
        return f
    m = m % (len(str(m))*10)
    print('n = ', fib_digit(n))
    print('m = ',m)
    print('n/m = ',fib_digit(n) / m)
    return fib_digit(n) % m

print(fib_mod(15, 33))