from functools import wraps

def p_decorate(func):
    def func_wrapper(*args,**kwargs):
        return "<p>{0}</p>".format(func(*args,**kwargs))
    return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name + " " + self.family

my_person = Person()

print(my_person.get_fullname())


def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}<{0}>".format(tag_name,func(name))
        return func_wrapper
    return tags_decorator

@tags("p")
def get_text(name):
    return "Hello " + name

print(get_text("John"))

"""
functools wraps
"""

def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}<{0}>".format(tag_name,func(name))
        return func_wrapper
    return tags_decorator

@tags("str")
def get_text(name):
    """returns some text"""
    return "Hello " + name

print(get_text.__name__) # get_text
print(get_text.__doc__) # get docstring
print(get_text.__module__) # get module
