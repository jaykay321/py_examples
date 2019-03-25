def multiply_of(n):
    def mulitplier(number):
        return number*n
    return mulitplier

multiplywith5 = multiply_of(4)
print(multiplywith5(9))
