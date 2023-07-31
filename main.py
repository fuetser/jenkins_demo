a = []


def fib(n):
    if n <= 2:
        return 1
    a.append(n)
    return fib(n - 1) + fib(n - 2)


fib(1000)
