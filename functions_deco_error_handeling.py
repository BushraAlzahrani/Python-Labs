def addition(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)
 
try:
    addition(10, 20) 
except NameError as ne:
    print(ne.__class__)
else:
    print('The operation is successful')


# creating the decorater

def string_deco(func):
    def wrapper(*args):
        if [n for n in args if type(n) == str and len(n) > 5 ]:
            return func(*args)
        else:
           raise ValueError ('should be str and it should have more than 5 characters')     
    return wrapper


@string_deco
def print_word(word):
    print(word)

try:
    print_word('eduction')

except ValueError as v:
    print(v)