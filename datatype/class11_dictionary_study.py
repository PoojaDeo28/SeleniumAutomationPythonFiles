#Dictionary data type
a={'name':'pooja','age':'30','rollno':430}
print('Dictionary',a)
print(type(a))
print('keys: ',a.keys())
print('values:',a.values())
#display value of particular key
print(a["name"])                    #pooja
print(dir(a))
g={1:[20,30]}
print('dic with multiple ',g)
#f={[10,20]:1}               #shows error, keys can not two
#print('dic',f)
#copy
b=a.copy()
print('copied dictionary: ',b)

#fromkeys
'''Imp points:-

1.Duplicate keys are not allowed but values can be duplicated.
2.Hetrogeneous object are allowed for both key and values.
3.Insertion order is not preserved.
4.Dictionary are mutable.

Note:- In  C++ and java Dictionary are known as 'Map' and
 in perl and Rubby known as 'hash'

'''

#clear
#delete
#fromkeys
a = ('Delhi','BLG','HYD','BBSR')
b=('Raghav')
c=dict.fromkeys(a,b)
print('dictionary using form keys: ',c)
#get
c={'name':'pooja','age':30,'city':'delhi'}
print('dictionary c',c)
name=c.get('name')
print('name: ',name)
#items
items1=c.items()
print('display items: ',items1)
#keys
a={'name':'pooja','age':30,'city':'delhi'}
print(a.keys())
#values
print(a.values())
#POP(key)
print('poped element: ',a.pop('city'))
print('dictionary after poping: ',a)        #dictionary after poping:  {'name': 'pooja', 'age': 30}
#a.pop('pincode')            #shows error when trying to pop non-present key
#popitem                        #pops last key and value
print(a.popitem())    #('age', 30)
print('dict. after last element poped: ',a)      #dict. after last element poped:  {'name': 'pooja'}
#pop items from empty dictionary
b={}
#b.popitem()                     #gives error, can not pop element from empty list
#setdefault
a={'name':'pooja','age':30,'city':'delhi'}
print('new dict: ',a) #new dict:  {'name': 'pooja', 'age': 30, 'city': 'delhi'}
a.setdefault('zipcode',123456)
print('after adding new key-value pair',a)
a.setdefault('city','mumbai')      # after adding new key-value pair {'name': 'pooja', 'age': 30, 'city': 'delhi', 'zipcode': 123456}
a.setdefault('district','Delhi')  #{'name': 'pooja', 'age': 30, 'city': 'delhi', 'zipcode': 123456, 'district': 'Delhi'}
print(a)



