#Tuple data type
#immutable,other things as same as list
#elements closed in parathesis()
s=(1,2,3,4,3)
print('tuple',s)                    #tuple (1, 2, 3, 4)
print('type',type(s))               #type <class 'tuple'>
print(dir(s))
#note: tuple is read-only version of list.
s1=s.count(3)
print('count(): ',s1)
s2=s.index(3)
print('index function:',s2)

#set data type
#no order of insersion
#no duplicates
#elements closed in curly brackets
#no concept of index
#heterogenose allowed
#mutable datatype
#growable in nature
s= {1,1,2,2,2,3,4,'scodeen',True,(78,90)}
print('set',s)
print('type: ',type(s))
#set manipilation
s={1,2,3,4,5,6,7}
print(dir(s))
#add
s.add(8)
print('after adding 8:',s)     #after adding 8: {1, 2, 3, 4, 5, 6, 7, 8}
#clear
#copy
s1=s.copy()                     #Create a mirror image in other variable.
print('copied set: ',s1)        #copied set:  {1, 2, 3, 4, 5, 6, 7, 8}
print('original set: ',s)
s.add(9)
s.add(10)
s.add(11)
print(s)
difference_set=s.difference(s1)
print('difference: ',difference_set)      #  difference:  {9, 10, 11}
difference_set2=s1.difference(s)
print('difference_2: ',difference_set2)     #difference_2:  set()
#discard
s1.discard(6)
print('after discarding 6: ',s1)
s1.discard(100)
print('after discarding non-exist element',s1)   #no change in set
#pop:- removes random element
s3={234,5,52,87,3424,3414,1213,242,5,1324,9,8978,13}
print('s3:',s3)
print('popped element: ',s3.pop())     #popped element:  3424
print('popped element: ',s3.pop())      #popped element:  5
print('popped element: ',s3.pop())      #popped element:  9
print('popped element: ',s3.pop())      #popped element:  234
d={}   #empty set is dictionary, not set
print(type(d))              #<class 'dict'>
#remove:-doen not return removed element
s3.remove(13)
print('removed element 13: ',s3)
#s3.remove(5)
print('removed element 5: ',s3)   #gives error
#intersection
s1={1,3,4,5,8,9}
s2={1,5,0,34}
intersection_set1=s1.intersection(s2)
print('intersection of s1 & s2',intersection_set1)   #intersection of s1 & s2 {1, 5}
intersection_set2=s2.intersection(s1)
print('intersection of s2 & s1',intersection_set2)      #intersection of s2 & s1 {1, 5}
#union
union1=s1.union(s2)
print('union of s1 & s2',union1)     #union of s1 & s2 {0, 1, 34, 3, 4, 5, 8, 9}
union2=s2.union(s1)
print('union of s2 & s1',union2)    #union of s2 & s1 {0, 1, 34, 3, 4, 5, 8, 9}
union3=s1.union(s1)
print('union with itself',union3)   #union with itself {1, 3, 4, 5, 8, 9}

#update

d={4,5,6}
d1={7,8}
d.update(d1)
print('update: ',d)         #update:  {4, 5, 6, 7, 8}
'''Update() method takes only a single argument.
 The single argument can be a set, list, tuples or a dictionary. 
It automatically converts into a set and adds to the set. '''
fs=frozenset(s3)
print('frozen set of s3: ',fs)      #frozen set of s3:  frozenset({242, 8978, 52, 3414, 87, 1324, 1213})
s6=fs.copy()
print('s6',s6)                      #s6 frozenset({242, 8978, 52, 3414, 87, 1324, 1213})
l1=[233,123,123]
fs_list=frozenset(l1)
print('forzen set of list',fs_list)
my_list=list(fs_list)
print('frozen set into list: ',my_list)
set1=set(fs_list)
print('frozen set into set: ',set1)
print(dir(fs_list))


