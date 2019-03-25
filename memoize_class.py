class Memoize(object):
    def __init__(self,f):
        self.f = f
        self.memo = {}

    def __call__(self,*args):
        if not args in self.memo:
            self.memo[args] = self.f(args)
        return self.memo[args]


def factorial(k):
    k_temp = k[0]
    if k_temp < 2:
        return 1
    return k_temp * factorial(k_temp-1)

factorial = Memoize(factorial)

print(factorial(10))
