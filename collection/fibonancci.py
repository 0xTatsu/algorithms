# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
# input: Index
# output: the number at that index


def fib(n):  # bad solution
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


def fib2(n):
    fib = [0, 1]
    for _ in range(2, n+1):
        fib.append(fib[-1] + fib[-2])
    return fib[n]


def fib3(n):
    current = 0
    after = 1
    for _ in range(0, n):
        current, after = after, current + after
    return current


def fib4(n):
    a = ((1 + (5 ** 0.5)) / 2)**int(n)
    b = ((1 - (5 ** 0.5)) / 2)**int(n)  # 0.002
    return round((a - b) / (5 ** 0.5))
    # Because b is too small so that we can ignore it
    # return round((((1+(5**0.5))/2)**int(n))/(5**0.5))


print(fib4(6))
