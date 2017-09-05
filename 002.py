# Задача на программирование повышенной сложности: огромное число Фибоначчи по модулю
# Даны целые числа 1≤n≤10^18 и 2≤m≤10^5, необходимо найти остаток от деления n-го числа Фибоначчи на m.

# Решение на работает для чисел Фибоначи, оканчивающихся на 0.

def fib_mod(n, m):

    def fib(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        s0 = 0
        s1 = 1
        for i in range(n - 1):
            s = s0 + s1
            s0 = s1
            s1 = s
        return s

    def fib_digit(n): # берём функцию нахождения последней цифры n-го числа Фибоначи из предыдущей задачи 001.
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
    m = m % 10
    print('n = ', fib_digit(n))
    print('n0 = ', fib(n))
    print('m = ',m)
    print('n/m =',fib_digit(n) / m, ' n%m =', fib_digit(n) % m, fib_digit(n) // m, ' n0%m =',fib(n) % m)
    return fib_digit(n) % m

print(fib_mod(10, 33))