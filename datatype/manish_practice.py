'''s='scodeen'
print('given string: ',s)
a=s[0:3]
print('ans a: ',a)   #first 3 characters

b=s[4:]
print('ans b: ',b)    #last 4 characters

c=s[:3]
print('ans c: ',c)   #first 3 characters

d=s[:]
print('ans c: ',d)   #entire string
'''
name='Shanaya London'
dob='25-11-2015'
first_slice=name[:7]
print('first name:  ',first_slice)


second_slice=name[8:14]
print('city: ',second_slice)

dob_month_slice=dob[3:5]
print("birth month:",dob_month_slice)

dob_date_slice=dob[:2]
print('dob date:',dob_date_slice)

dob_date_year=dob[6:]
print('dob year:',dob_date_year)

rev_slice=name[0:-3]
print('reverse city:',rev_slice)

stmt='i love my country'
s1=stmt[0:-2:1]
print('s1:',s1)

s2=stmt[0:-1:3]
print('s2:',s2)

s3=stmt[2:14:3]
print('s3:',s3)

s4=stmt[3:15:3]
print('s4:',s4)

s5=stmt[2:16:3]
print('s5',s5)

s6=stmt[3:16:4]
print('s6:',s6)
print(stmt)

s7=stmt[-14:-1:3]
print('s7:',s7)
print(dir(stmt))

print(dir(stmt))
print(type(stmt))

