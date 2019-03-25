
n = 10
cache = [None]*(n+1)

def fib(n):
    if n > 10:
        cache.extend([None]*(n-10))
    if n < 2:
        return n

    if cache[n] != None:
        return cache[n]

    else:
        cache[n] = fib(n-2) + fib(n-1)
        return cache[n]

print(fib(14))
