print('ans 1:')
print( "Twinkle, twinkle, little star,\n\tHow I wonder what you are!n\n\t\tUp above the world so high,"
       "\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,"
       "\n\tHow I wonder what you are")

'''2. Write a Python program to get the Python version you are using.'''
import sys
print('python version: ',sys.version)
print('version info:',sys.version_info)

'''3. Write a Python program to display the current date and time.'''

import datetime
now=datetime.datetime.now()
print('ans 3:current date and time:' ,now)
print(now.strftime('ans 3:%Y-%m-%d %H:%M:%S'))

'''4. Write a Python program which accepts the radius of a circle from the user and compute the area.'''
from math import pi
#radius=float(input('enter radius'))
#area=pi*radius*radius
#print('area of circle: ',area)

'''5.Write a Python program which accepts the user's first and last name 
and print them in reverse order with a space between them. '''
'''fname=input('please enter first name: ')
lname=input('please enter last name: ')
print('ans 5: ',fname,'',lname)'''

'''6. Write a Python program which accepts a sequence of comma-separated numbers from user
 and generate a list and a tuple with those numbers.'''
'''numbers=input('input numbers: ')
list_numbers=numbers.split(',')
tuple_numbrs=tuple(list_numbers)
print('ans 6:List of numbers:',type(list_numbers),list_numbers)
print('ans 6:tuple of numbers:',type(tuple_numbrs),tuple_numbrs)'''

'''8.Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]'''
color_list = ["Red","Green","White" ,"Black"]
print('ans 8: first color:',color_list[0],'','last color:',color_list[-1])

'''9.Write a Python program to display the examination schedule. 
(extract the date from exam_st_date). '''
exam_st_date = (11, 12, 2014)

print('ans 9:exam will start from: %i / %i / %i '%exam_st_date)

'''10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.'''
'''n=int(input('enter number: '))
addition=n+n*n+n*n*n
print('values of',n,'is:',addition)'''

'''11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
'''
print('ans 11:')
print(abs.__doc__)

'''12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
'''
'''import  calendar
y=int(input('input the year: '))
m=int(input('input the month: '))
print('ans 12: year and month')

print(calendar.month(y,m))'''

'''13. Write a Python program to print the following 'here document'. 
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example'''
print("""a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example""")

'''14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days'''

from datetime import date
f_date=date(2014, 7, 2)
l_date=date(2014, 7, 11)
diff_date=l_date-f_date
print(diff_date.days)

'''15. Write a Python program to get the volume of a sphere with radius 6'''
'''import math
radius=6
volumn_spehere=4/3*pi*radius**3
print('ans 6: Volume of Spehere',volumn_spehere)'''

'''16. Write a Python program to get the difference between a given number and 17, 
if the number is greater than 17 return double the absolute difference. '''

'''x=int(input('enter number: '))
if x>=17:
       d1=x-17
       print('ans 16: Difference is: ',d1*2)
else:
       d2=17-x
       print('ans 16:difference is',d2)'''

'''18. Write a Python program to calculate the sum of three given numbers, 
if the values are equal then return three times of their sum.'''
'''a=int(input('enter first number: '))
b=int(input('enter second number: '))
c=int(input('enter third number: '))
if a==b and b==c:
       print('ans 18: cube: ',a*a*a)
else:
       print('ans 18: product of 3 numbers: ',a*b*c)'''

'''20. Write a Python program to get a string which is
 n (non-negative integer) copies of a given string.'''
'''str1=input('enter string: ')
no_of_copies=int(input("enter number: "))
if no_of_copies<=0:
       print('ans 20: please enter positive number greater than 0')
else:
       result=""
       for i in range(no_of_copies):
              result=result+str1
       print('ans 20: ',result)'''

'''21. Write a Python program to find whether a given number (accept from the user) is even or odd,
 print out an appropriate message to the user. '''

'''number1=int(input('enter number: '))
if number1%2==0:
       print('ans 21: number is even')
else:
       print('ans 21: number is odd')
       '''

'''22. Write a Python program to count the number 4 in a given list. '''
list1=[4,5,6,4,6,7,9]
count_of_4=list1.count(4)
print('ans 22: number of 4 in list: ',count_of_4)

'''23. Write a Python program to get the n (non-negative integer) copies of the first 2 
characters of a given string. 
Return the n copies of the whole string if the length is less than 2. '''
'''origin_string='myname is pooja'
first2_char=origin_string[:2]
no_of_copies=int(input('enter number: '))
str_copies=""
for i in range(no_of_copies):
       str_copies=str_copies+first2_char
print('ans 23:',str_copies)'''

'''24. Write a Python program to test whether a passed letter is a vowel or not'''


'''25. Write a Python program to check whether a specified value 
is contained in a group of values.'''
list2=[1,2,3,4,5]
'''n=int(input('enter number: '))
for value in list2:
       if n==value:
              print('ans 25: your number is in list')
       else:
              print('ans 25: your number is not in list')
#status : half done'''
'''26. Write a Python program to create a histogram from a given list of integers.'''

'''(this Q is in not from basic practice)30. Write a Python program to get the frequency 
of the elements in a list. '''
print('ans 30: original list',list1)
for i in list1:
       count_of_i=list1.count(i)
       print('count of {}'.format(i),':',count_of_i)

'''(this Q is not from basic practice)31. Write a Python program to count the 
number of elements in a list within a specified range.'''
list3=[123,234,345,345,5,7,678,78,78,979,13]
'''range_number=int(input('enter range: '))
for i in range(range_number):
       break
print(len(list3))'''

#status: done

'''27. Write a Python program to concatenate all elements in a list into a string and return it.'''
list_words=['i','love','my','India']
result=''
for words in list_words:
       result +=' '+str(words)
print('ans 27:',result)

'''28. Write a Python program to print all even numbers from a given numbers list
 in the same order and stop the printing if any numbers that come after 237 in the sequence.'''


numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]
even_list=''
for even_numbers in numbers:
       if even_numbers==237:
              print(even_numbers)
              break
       elif even_numbers%2==0:
              print(even_numbers)

'''29. Write a Python program to print out a set containing 
all the colors from color_list_1 which are not present in color_list_2.'''
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print('ans 29: ',color_list_1.difference(color_list_2))

'''30. Write a Python program that will accept the base and height 
of a triangle and compute the area. '''
'''base=float(input('enter base: '))
hight=float(input('enter hight: '))
area=0.5*base*hight
print('ans 30: Area of Triangle: ',area)'''
#q30 status: done
'''31. Write a Python program to compute the greatest common divisor
 (GCD) of two positive integers.'''
'''x=int(input('enter first number'))
y=int(input('enter second number'))
x_factors={1}
for i in range(1,x+1):
    if x%i==0:
        x_factors.add(i)
    else:
        i+=i
print('factors of {}'.format(x),':',x_factors)
y_factors={1}
for j in range(1,y+1):
    if y%j==0:
        y_factors.add(j)
    else:
        j+=j
print('factors of {}'.format(y),':',y_factors)
gcd=max(x_factors.intersection(y_factors))
print('ans 31: GCD of {}'.format(x),'and {}'.format(y),'is: ',gcd)'''
#q31 status: done

'''32. Write a Python program to get the least common multiple (LCM) of two positive integers.'''
'''x1=int(input('enter first number: '))
y1=int(input('enter second number: '))
if x1>y1:
    z=x1
else:
    z=y1
while(True):
    if((z%x1==0) and (z%y1==0)):
        lcm=z
        break
    z+=1
print(lcm)'''
#q33 staus: done

'''33. Write a Python program to sum of three given integers.
 However, if two values are equal sum will be zero.'''
'''x2=int(input('enter first number'))
y2=int(input('enter second number'))
z2=int(input('enter third number'))

if x2==y2 or y2==z2 or x2==z2:
    sum = 0
    print('ans 33: if any two numbers are same: sum=',sum)
else:
    sum=x2+y2+z2
    print('ans 33: if all numbers are different: sum=',sum)'''
#q 33 status: done
'''34. Write a Python program to sum of two given integers. 
However, if the sum is between 15 to 20 it will return 20.'''
'''x3=int(input('enter first number: '))
y3=int(input('enter second number: '))
sum=x3+y3
if sum>=15 and sum<=20:
    print('ans 34: sum:  ',20)
else:
    print('ans 34: sum: ',sum)'''

#q34 status: done

'''35. Write a Python program that will return true if the two given integer values are equal
 or their sum or difference is 5. '''
'''x4=int(input('enter first number'))
y4=int(input('enter second number'))
sum=x4+y4
if x4==y4 or abs(x4-y4)==5 or sum==5:
    print('ans 4: ',True)
else:
    print('ans 4: ', False)
'''
#q35 status: done

'''36. Write a Python program to add two objects if both objects are an integer type.'''
'''x5=eval(input('enter first number: '))
y5=eval(input('enter second number: '))
print(type(x5))
if not(isinstance(x5,int) and isinstance(y5, int)):
    print('ans 36: numbers must be integers')
else:
    sum=x5+y5
    print('ans 36: sum of intergers: ',sum)'''
#q36 status: done

'''37. Write a Python program to display your details like name, age, address
 in three different lines.'''
name,age,address='Pooja',30,'Delhi, Mumbai, London'
print('ans 37: ','Name:',name,'\nAge: ', 19,'\nAddress:',address)

'''38. Write a Python program to solve (x + y) * (x + y). 
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49'''
x6,y6=4,3
result=x6*x6+2*x6*y6+y6*y6
print('ans 38: result of ({}+{})^2): '.format(x6,y6),result)

'''39. Write a Python program to compute the future value of a specified principal amount, 
rate of interest, and a number of years.'''
#Test Data : amt = 10000, int = 3.5, years = 7   #Expected Output : 12722.79
amt=10000
interest=3.5
years=7
future_value=amt*((1+(0.01*interest))**years)
print('ans 39: Future amount: ',round(future_value,2))

'''40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).'''
import math
p1=[4,0]
p2=[6,6]
distance=math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
print('ans 40: Distance between two points: ',distance)

#q40 status: done

'''41. Write a Python program to check whether a file exists.'''
import os.path
print('ans 40: file existance: ',os.path.isfile('main.txt'))
print('ans 40: file existance: ',os.path.isfile('main.py'))
'''file_name=input('enter file name: ')
print('ans 40: file existance: ',os.path.isfile(file_name))'''

#q41 status: done

'''42. Write a Python program to determine 
if a Python shell is executing in 32bit or 64bit mode on OS.'''
import struct
print('ans 42: ',struct.calcsize("P") * 8)

'''43. Write a Python program to get OS name, platform and release information.'''
import platform
import os
print('ans 43: Name of operating system: ',os.name)
print('ans 43: Name of OS system: ',platform.system())
print('ans 43: Version of operating system: ',platform.release())

'''44. Write a Python program to locate Python site-packages'''
import site
print(site.getsitepackages())
#q44 status: done

'''45. Write a Python program to call an external command. '''
'''from subprocess import call
call(["ls", "-l"])'''

#q45: error

'''46. Write a python program to get the path and name of the file that is currently executing.'''
import os
print('ans 46: file path',os.path.relpath(__file__))
#q46 status: done

'''47. Write a Python program to find out the number of CPUs using.'''

import multiprocessing
print('ans 47: ',multiprocessing.cpu_count())
#q47 status: done

'''48. Write a Python program to parse a string to Float or Integer. '''
'''parse_string=input('enter string: ')
print('ans 48: ',float(parse_string))
print('ans 48: ',int(float(parse_string)))'''

#q48 status: done
'''49. Write a Python program to list all files in a directory in Python.'''
'''from os import listdir
from os.path import isfile,join
files_list = [f for f in listdir('/SoftwareTesting/python') if isfile(join('/SoftwareTesting/python', f))]
print(files_list);'''

#q49 status: error in file path
'''50. Write a Python program to print without newline or space.'''
print('ans 50:')
for i in range(0,10):
    print('*',end='')
print("\n")
for i in range(0,10):
    print('*',end='/')
print("\n")

'''51. Write a Python program to determine profiling of Python programs. '''
import cProfile
def sum():
    print(1+2)
print('ans 51:')
cProfile.run('sum()')

'''53. Write a python program to access environment variables.'''
import os
print('*----------ANS 53-------------*')
print(os.environ)
print(os.environ['HOMEDRIVE'])
print(os.environ['PATH'])
print(('*----------------------*'))

'''54. Write a Python program to get the current username. '''
import getpass
print('ans 54: ',getpass.getuser())

'''55. Write a Python to find local IP addresses using Python's stdlib. '''

'''58. Write a Python program to sum of the first n positive integers. '''
'''numbers=int(input('enter number: '))
sum=int((numbers*(numbers+1))/2)
print('sum of first {} numbers: '.format(numbers),sum)'''

'''59. Write a Python program to convert height (in feet and inches) to centimeters.'''
height_feet=int(input('Enter feet: '))
height_inches=int(input('Enter inches: '))
height_inches+=height_feet*12
height_cm=round(height_inches*2.54,1)
print('Height in cm: ',height_cm)



