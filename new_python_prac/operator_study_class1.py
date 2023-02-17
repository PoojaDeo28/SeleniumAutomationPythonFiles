#Types of Operator
'''1.Arithmetic Operator --> +,-,*,/,%,//,**
2.Comparision Operator /conditional operator ,<>=<=,!= ==
3.Logical Operator  and or not
4.Membership Operator in not in
5.Assigment Operator =,+=,-=,*=,/=
6.Identity Operator is ,not is
7.Bitwise Operator &  |  symbolic
8.ternary Operator --> abhi nahi  control statement'''


import math
print(math.ceil(106.85))
print(2**4)
print(math.sqrt(4))
a=45
b=90
print(a<b)

a='test.pdf'
b=45
c=90
print(c>b and a.startswith('t'))#true
print(c>b and a.startswith('k'))#false
print(True and True and True and False) #false

#membership operator(in, not in) is used for collection/group data types like list, tuple,set, dict,str
py_list=[45,86,24,97,3,'python','ml']
print(100 in py_list)   #false
print(45 in py_list)    #True
print('p' in 'Python')  #false
print(100 not in py_list)  #true
print('ml' not in py_list) #false

#assignment operator: +=,-=,*=,/=

a=10
b=10
print(a is b)  #true
print(a is not b) #false
a=984284
b=984284
print(a is b)  #true

# bitwise operator
print(45 & 6)




