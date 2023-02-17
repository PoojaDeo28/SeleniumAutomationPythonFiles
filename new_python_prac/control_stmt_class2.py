'''simple if
if-else
if -else ladder
nested if-else'''

'''simple if:-
only one condition
if condition:
    body'''
print('welocme to dose chaeking program')
age=int(input("enter the age:"))
if(age>50):
    print("please take booster on priority")
print('thanks')


email=input('enter your email id: ')
if email.endswith("gmail.com"):
    print(f"given mail--->{email} is valid mail")
print('thanks for checking mail')

no=int(input('enter number: '))
if(no%2==0):
    print(f"number {no} is even")
else:
    print(f"number {no} is odd")

filename=input('enter file: ')
if filename.split('.')[1] in ['pdf','xsls','txt','doc']:
    print('your file is processing...')
else:
    print('please enter valid file name...')