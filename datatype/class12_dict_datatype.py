di={'name':'krishna','address':'krishnarajpuram','phone':[2323,13213],'award':9}
print('dictionary: ',di)
# copy
copy_dm=di.copy()
print('copied list: ',copy_dm)

#fromkeys
name=['pooja','shanaya','gaurav','inaya']
package='12LPA'
new_di=di.fromkeys(name,package)
print('new list: ',new_di)

#get
print('phoneno',di.get('phone'))

#items
print('Dictionary items: ',di.items())

#keys
print('Dictionary keys: ',di.keys())

#values
print('Dictionary values: ',di.values())

#pop
di.pop('award')
print('dictionary after poping award key: ',di)

#popitem
di.popitem()
print('dictionary after poping last key: ',di)

#setdefault
di.setdefault('subject','python')
print('dictionary after adding new key',di)

#update
new={'company':'infosys','year':4}
di.update(new)
print('updated list: ',di)

#changing value of key from old to new
di['name']='pooja'
print('changing name from krishna to pooja',di)