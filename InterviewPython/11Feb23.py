def function_decorator(func):
    def wrapped_func():
        print('=' * 30)
        func()
        print('=' * 30)
    return wrapped_func
#Then, let’s use this decorator.

@function_decorator
def test():
    print('Hello World!')
test()

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




# generator
#def cal(a,b):
#    sum=a+b
#    sub=a-b
#    mul=a*b
#   div=a/b

#   yield sum
#    yield sub
#    yield mul
#    yield div

#result=cal(10,20)
#print(type(result))

#print(next(result))
#print(next(result))
#print(next(result))
#print(next(result))


def add(*args):
    total=0
    for i in args:
        total=total+ i
    return total

print(add(10,40))


#filter

li=[123,24,46,67]
var=list(filter(lambda a: a%2==0,li))
print(var)

f=open(r"E:\Pooja\SoftwareTesting\InterviewNotes\file_reading.txt","a")
f.write("this is software testing,sdsddds")
f.close()

f1=open(r"E:\Pooja\SoftwareTesting\InterviewNotes\file_reading.txt","r")
#print("read: ",f1.read())
#print("read(n): ",f1.read(4))
#print("readline: ",f1.readline(7))
#print("readlines: ",f1.readlines())
#f=open("E:\\Pooja\\SoftwareT
# esting\\InterviewNotes\\file_reading.txt","r")
#print(f.read())


var=[i*i for i in range(1,11)]
print(var)