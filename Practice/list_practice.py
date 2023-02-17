list1=[23,24,56,13,354]
print(list1)
'''1. Write a Python program to sum all the items in a list.'''
sum=sum(list1)
print('ans1: sum:', sum)
sum1=0
for x in list1:
    sum1 +=x
print('ans1: sum using for loop: ',sum1)
#q1 status: done
'''2. Write a Python program to multiply all the items in a list.
'''
multiply=list1[0]*list1[1]*list1[2]*list1[3]*list1[4]
print('ans2: multiplication:',multiply)
tot=1
for i in list1:
    tot *=i
print('ans2: multiplication using for loop: ',tot)
#q2 status: done
'''3. Write a Python program to get the largest number from a list. '''
list1.sort();
print('ans3: largest element: ',list1[-1])
#q3 status: done
'''4. Write a Python program to get the smallest number from a list.'''
list1.sort()
print('ans4: smallest element: ',list1[0])
#q4 status: done
'''5.Write a Python program to count the number of strings where the
 string length is 2 or more and the first and last character are
  same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']'''
List2 = ['abc', 'xyz', 'aba', '1221','131']
print(List2)
#def match_words(List2):
count_var=0
for i in List2:
    if len(i)>1 and i[0] == i[-1]:
        count_var +=1
print('ans 5 :',count_var)
#q5 status: done
#print(match_words(List2))
'''6. Write a Python program to get a list, sorted in increasing
 order by the last element in each tuple from a given list of
  non-empty tuples.'''
list_tuple=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#q6 status: not done
'''7. Write a Python program to remove duplicates from a list. '''
list7=[323,232,323,143,4667,1,1]
#print(list7)
unique_list7=[]
unique_set7=set(list7)
list7=list(unique_set7)
print('ans7:, unique list',list7)
#q7 status: done
'''8. Write a Python program to check a list is empty or not.'''
print(len(list7))
if len(list7)>0:
    print('ans 8: list is not empty')
else:
    print('ans 8:list is empty')
#q8 status: done
'''9. Write a Python program to clone or copy a list.'''
list9=list7.copy();
print('ans 19: copid list:', list9)
#q9 status: done

'''10. Write a Python program to find the list of words that are 
longer than n from a given list of words.'''
list10=['words','that','are', 'longer','than','from','a','given','list','of','jsdh']
#q10 status: not done
#print(len(int(list10[0])))
'''11. Write a Python function that takes two lists and returns 
True if they have at least one common member. '''
list11=[22,23,24,25]
list12=[23,22,78,79,45]
set1=set(list11)
set2=set(list12)
set_intersection=set1.intersection(set2)
if len(set_intersection) > 0:
    print('ans 11:true')
else:
    print('ans 11: false')
    #q11 status: done

'''12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.'''
color= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

#q12 status: not done

'''13. Write a Python program to generate a 3*4*6 3D array whose each element is *. '''

'''14. Write a Python program to print the numbers of a specified
 list after removing even numbers from it. '''
list11=[i for i in list11 if i%2!=0]
print('ans 14: ',list11)
#q14 status: done

'''15. Write a Python program to shuffle and print a specified list.'''
import random
random.shuffle(list12)
print('ans 15: ',list12)
#q15 status: done
'''16.Write a Python program to generate and print a list of first and last 5 elements 
where the values are square of numbers between 1 and 30 (both included).'''
l = list()
for i in range(1,31):
	l.append(i**2)
print('ans 16: first 5 elements: ',l[:5])
print('ans 16: first 5 elements: ',l[-5:])
#q16 status: done
'''17. Write a Python program to generate and print a list except for the first 5 elements, 
where the values are square of numbers between 1 and 30 (both included).'''
l1=list()
for i in range(1, 31):
    l.append(i**2)
print('ans 17: ',l[5:])
#q17 status: done
''''''

import itertools
print('ans 18: List permutations: ',list(itertools.permutations([1,2,3])))
#q18 status: done
'''19. Write a Python program to get the difference between the 
two lists. '''
list_diff1=[1,2,3]
list_diff2=[3,4,5]
diff_list1_list2=list(set(list_diff1)-set(list_diff2))
diff_list2_list1=list(set(list_diff2)-set(list_diff1))
tot_diff=diff_list1_list2+diff_list2_list1
print('ans 19: Difference ',tot_diff)
#q19 status: done

'''20. Write a Python program access the index of a list.'''
for i in list10:
    print('indices for',i,':',list10.index(i))

'''21. Write a Python program to convert a list of characters 
into a string. 
'''
string1=""

string1=' '.join(list10)
print(string1)

'''22. Write a Python program to find the index of an item in a 
specified list. '''
print('index of than is:',list10.index('than'))
'''23. Write a Python program to flatten a shallow list.'''

shallow_list1=[2,4,3]
shallow_list2=[1,5,6]
shallow_list3=[9]
shallow_list4=[7,9,0]
flatten_list=shallow_list1+shallow_list2+shallow_list3+shallow_list4
print('ans 23:Flatten list by adding',flatten_list)
#q23 status: done
'''24. Write a Python program to append a list to the second list.'''
list14=[1234,234,456]
list15=[35,56,567]
for i in list15:
    list14.append(i)
print('ans 24: combined 2 lists: ',list14)
#q24 status: done

'''25. Write a Python program to select an item randomly 
from a list.'''
print('ans 25: randome element:',random.choice(list14))
#q25 status: done
'''26. Write a python program to check whether two lists are circularly identical. '''

'''27. Write a Python program to find the second smallest number in a list. '''
list14.sort()
print('ans 27: second smallest element:',list14[1])
#q25 status: done
'''28. Write a Python program to find the second largest number in a list. '''
print('ans 28: second largest element:',list14[-2])
#q28 status: done
'''29. Write a Python program to get unique values from a list.'''
list16=[23,23,53,43,34,43]
list16_set=set(list16)
list16=list(list16_set)
print('ans 29: Unique items of list:',list16)
#q29 status: done
'''30. Write a Python program to get the frequency of the elements in a list.'''
list17=[23,23,53,43,34,43]
frequeny=list17.count(23)
print('ans 30: frequency of 23:',frequeny)
#q30 status: done
'''31. Write a Python program to count the number of elements in a list within a specified range.'''
#q31 status: not done

'''32. Write a Python program to check whether a list contains a sublist.'''

'''33. Write a Python program to generate all sublists of a list.'''

'''34. Write a Python program using Sieve of Eratosthenes method for computing primes
 upto a specified number. '''

'''35. Write a Python program to create a list by concatenating a given
 list which range goes from 1 to n. '''

'''36. Write a Python program to get variable unique identification number or string.'''
x=23
print('ans 36: id of variable: ',id(x))

y='pooja'
print('ans 36: id of string',id(y))
#Q36 status: done
'''37. Write a Python program to find common items from two lists. '''
list_intersect1=[12,23,345,45,345]
list_intersect2=[12,45,3424,24234,35]
list1_common=set(list_intersect1).intersection(set(list_intersect2))
print('ans 37: list common elements: ',list(list1_common))
#q37 status: done

'''38. Write a Python program to change the position of every n-th value with the (n+1)th 
in a list.'''

'''39. Write a Python program to convert a list of multiple integers into a single integer.'''
list_join=[123,123,6,23]
x=int("".join(map(str,list_join)))
print('ans 39 :',x)
#q39 status: done

'''40. Write a Python program to split a list based on first character of word. '''


'''41. Write a Python program to create multiple lists.'''
obj={}
for i in range(1,21):
    obj[i]=[]
print('ans 40: create multiple lists: ',obj)
#q41 status: done

'''42. Write a Python program to find missing and additional values in two lists. 
Sample data : Missing values in second list: b,a,c
Additional values in second list: g,h'''

list_42one=['a','b','c','d','e','f']

list_42two=['d','e','f','g','h']
missing_in_listTwo=set(list_42one).difference(set(list_42two))
print('ans 42: missing values in list1 ',list(missing_in_listTwo))
additional_in_listone=set(list_42two).difference(set(list_42one))
print('ans 42: additional values in list 2',list(additional_in_listone))
#q42 status: done

'''43. Write a Python program to split a list into different variables.'''
list43=['ad','ad','wr','tyu']
var1,var2,var3,var4=list43
print('ans 43:var1: ',var1)
print('ans 43:var1: ',var2)
print('ans 43:var1: ',var3)
print('ans 43:var1: ',var4)
list43_list=[[23,24],[2324,567],5678]
var5,var6,var7=list43_list
print('ans 43:var 5:',var5)
print('ans 43:var 6:',var6)
print('ans 43:var 7:',var7)

'''44. Write a Python program to generate groups of five consecutive numbers in a list. '''


'''45. Write a Python program to convert a pair of values into a sorted unique array.'''
list_sorted_array=[123,54,456,12,6435,54]
sorted_array=sorted(set(list_sorted_array))
print('ans 45: sorted_array',sorted_array)
'''46. Write a Python program to select the odd items of a list.'''
list1_odd=[1,2,3,4,8,6,7,8,12,10]
print('ans 46:odd index values: ',list1_odd[::2])     #odd index values
print('ans 46:even index values: ',list1_odd[1::2])      #even index values

'''47. Write a Python program to insert an element before each element of a list.'''
list_insert=[123,2345,13,243,35]
i=0
for i in list_insert:
    list_insert.insert(i,0)
    i +=2
print(list_insert)

#q47 status: not done
'''48. Write a Python program to print a nested lists (each list on a new line) using the print() function. '''
color48=[['red','pink'],['green'],['blue']]
print('ans 48:')
for i in color48:
    print('\n'.join([str(i)]))

'''49. Write a Python program to convert list to list of dictionaries.
Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
Expected Output: [{'color_name': 'Black', 'color_code': '#000000'},
 {'color_name': 'Red', 'color_code': '#FF0000'}, 
 {'color_name': 'Maroon', 'color_code': '#800000'}, 
 {'color_name': 'Yellow', 'color_code': '#FFFF00'}]'''

colour_key=["Black", "Red", "Maroon", "Yellow"]
colour_code_value=["#000000", "#FF0000", "#800000", "#FFFF00"]
print('ans 49: list conversion into dictionary')
for i, j in zip(colour_key,colour_code_value):
    print([{'colour_name':i, 'colour_code_value':j}])

''' 50.Write a Python program to sort a list of nested dictionaries. '''
my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
print("Original List: ",my_list)
my_list.sort(key=lambda e: e['key']['subkey'], reverse=False)
print('ans 50: sorted sub-dictionaries',my_list)


'''53. Write a Python program to create a list with infinite elements.'''
import itertools
c = itertools.count()
print('ans 53: Infinite elements')
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

'''54. Write a Python program to concatenate elements of a list. '''
print('ans 54: Concatinate elements: ')
print('-'.join(color))
print(''.join(color))

'''56. Write a Python program to convert a string to a list.'''
string56='i love my india'
list_string=[]
for i in string56:
    list_string.append(i)
print('ans 56: convert string into list: ',list_string)

import ast
color ="['Red', 'Green', 'White']"
print('ans 56: ',ast.literal_eval(color))

'''57. Write a Python program to check if all items of a given list of strings is equal to a given string.'''
color1 = ["green", "orange", "black", "white"]
color2 = ["green", "green", "green", "green"]
print("ans 57: ")
print(all(c == 'blue' for c in color1))
print(all(c == 'green' for c in color2))

'''58. Write a Python program to replace the last element in a list with another list.
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]'''
list58_1=[1, 3, 5, 7, 9, 10]
list58_2=[2, 4, 6, 8,13]
list58_1.pop()
list58_1.extend(list58_2)
print('ans 58: new list: ',list58_1)

'''59. Write a Python program to check whether the n-th element exists in a given list. '''
xlen=len(list58_1)-1
print('ans 59: ',list58_1[xlen])
#or
print('ans 59: ',list58_1[-1])

''''''
