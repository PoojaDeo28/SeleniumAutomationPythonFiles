def decor(func):
    def inner_fun(*args):
        d=args[0]*args[1]
        return func(*args)
    return inner_fun

@decor
def calculator(a,b):
    c=a+b
    return c

print(calculator(10,20))
