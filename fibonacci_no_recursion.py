def fib(n):
    a,b = 0,1
    for i in range(n):
          a,b = b, a + b
    return a

print(fib(21))


def fib_iter(n):
    fib = {0:0, 1:1}
    if n > 1:
        for i in range(2,n+1):
            fib[i] = fib[i-2] + fib[i-1]
    return fib[n]

print(fib_iter(18))
