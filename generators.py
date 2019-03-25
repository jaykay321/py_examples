def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        print(answer)
        answer = "no" if answer == "yes" else "yes"

print(yes_or_no())
print(yes_or_no())
print(list(yes_or_no()))


def get_multiplies(number=3,count=10):
    x = 1
    counter = 0
    while counter < count:
        if x % number == 0:
            yield x
            counter += 1
        x += 1

print(list(get_multiplies()))
