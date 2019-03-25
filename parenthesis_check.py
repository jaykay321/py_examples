def parenthesis_check(s):
    opening_par = set('([{')
    matches = [('(',')'),('[',']'),('{','}')]
    stack = []

    for c in s:
        if c in opening_par:
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if (last_open, c) not in matches:
                return False
    return len(stack) == 0

s1 = "(())((()))"
print(parenthesis_check(s1))

s2 = "()())"
print(parenthesis_check(s2))
