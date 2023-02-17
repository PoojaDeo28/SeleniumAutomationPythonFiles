s='scodeen'
a=s[0:3]
print('ans a: ',a)                #sco
b=s[4:5]
print('ans b: ',b)                #een
c=s[:4]
print('ans c: ',c)                #scod
d=s[:]
print('ans d: ',d)                #scodeen

name='Shanaya London'
dob='25-11-2015'
first_slice=name[:7]
print("first slice:",first_slice)  #first slice: Shanaya
second_slice=name[8:14]
print("second slice:",second_slice) #second slice:London
dob_month_slice=dob[3:5]
print("birth month:",dob_month_slice) #birth month: 11
dob_date_slice=dob[:2]
print('dob date:',dob_date_slice) #dob date: 25
dob_year_slice=dob[6:10]
print('dob year:',dob_year_slice)#dob year: 2015
rev_slice=name[0:-7]
print('reverse city:',rev_slice) #reverse city: Shanaya
stmt='i love my country'
s1=stmt[0:-2:3]
print('s1:',s1)
s2=stmt[0:-1:3]
print('s2:',s2)
s3=stmt[2:14:3]
print('s3:',s3)
s4=stmt[3:15:3]
print('s4:',s4)
s5=stmt[2:16:3]
print('s5:',s5)
s6=stmt[3:16:4]
print('s6:',s6)
s7=stmt[-14:-1:3]
print('s7:',s7)
print(dir(stmt))