
cashe = {}

def fib(n):
    global cashe
    assert n >= 0
    if n not in cashe:
        cashe[n] = n if n <= 1 else fib(n - 1) + fib(n - 2)
        # print(cashe)
    return cashe[n]

print(fib(55))