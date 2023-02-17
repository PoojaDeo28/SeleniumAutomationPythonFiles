#list data type
l=[12,89,'gh',78.89,[56,89,90],(56,89),89]
print(type(l))                                #<class 'list'>
print(l[0])                                     #12
print(l[-1])                                    #89 last index element
print(l[1])                                     #89 second last element
print(l[-3])                                    #[56, 89, 90]
#imp functions
l=[10,20,30,40,50]
print(dir(l))
#len
print('length of list:',len(l))                #length of list: 5
#count
print('freq of given element: ',l.count(10))    #1
print('freq of given element: ',l.count(80))    #0
#index
print('index number of given element:',l.index(50))    #4
#print('index number of given element:',l.index(60))    #gives error
#manipulating functions
#append
l.append(60)                    #appends in last
print('appened list',l)         #appened list [10, 20, 30, 40, 50, 60]
#insert
l.insert(2,80)
print('inserted at 2:',l)       #inserted at 2: [10, 20, 80, 30, 40, 50, 60]
l.insert(99,91000)
print('wef',l)
print(l.index(91000))
l.insert(1000,88)
print('new item:',l)
print(l.index(88))
'''wef [10, 20, 80, 30, 40, 50, 60, 91000]
7
new item: [10, 20, 80, 30, 40, 50, 60, 91000, 88]
8
'''
#extend
l1=[1,2,3,4,5]
l2=[5,6,7,8,9]
l1.extend(l2)
print('l1:',l1)   #l1: [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
l3=['324',5,35.4345]
l4=['sd',234]
l4.extend(l3)               #l4 ['sd', 234, '324', 5, 35.4345]
print('l4',l4);
l5=[11,22,11,33,33,5,6,6]
l5.remove(33)
print('after removing 33: ',l5) #removes only one occurance,not duplicates
#after removing 33:  [11, 22, 11, 33, 5, 6, 6]
l5.remove(22)
print('after removing 22: ',l5) # after removing 22:  [11, 11, 33, 5, 6, 6]
#l5.remove(100)
print('after removing 100: ',l5)  #shows error
#pop() :-removes last
l5.pop()
print('after poping last element:', l5)   #after poping last element: [11, 11, 33, 5, 6]
l5.pop(-2)
print('pop second last element:',l5)        #pop second last element: [11, 11, 33, 6]
#l5.pop(60)
#print('pop 60th element: ',l5)             #error of out of range
#clear
l5.clear()
print('cleared list: ',l5)                  #cleared list:  []
#copy
a=[1,76,3,24,42,24]
b=a.copy()
print('copied list :',b)                    #cpoied list : [1, 76, 3, 24, 42, 24]

#reverse
b.reverse()
print('reversed list: ',b)
#sort
b.sort()
print('sorted list: ',b)
'''g=[5,'sfd',35,'qewwe']
g.sort()
print('sorted mixed list: ',g) '''     #TypeError: '<' not supported between instances of 'str' and 'int'

