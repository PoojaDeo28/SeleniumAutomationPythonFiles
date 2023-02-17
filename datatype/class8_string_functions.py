#1.captalize
s='shanaya'
print(s.capitalize())       #Shanaya
#count
print(s.count('a'))         #3
#endswith
print(s.endswith('a'))      #True
print(s.endswith('p'))      #False
print(s.endswith('3'))      #False
#startswith
print(s.startswith('s'))    #True
print(s.startswith('p'))    #False
print(s.startswith('5'))    #False
#replace
print(s.replace('shan','Mir'))  #Miraya
#find
print(s.find('y'))          #5
print(s.find('x'))          #-1
#format
#print(s.)
#index
print(s.index('n'))         #3
#print(s.index('x'))        #gives error
#join
p='*&'
print(s.join(p))          #*shanaya%shanaya#
print(s.join('456'))      #4shanaya5shanaya6
print('-'.join(s))
#lower
g='Pooja anil jagtap'
print(g.lower())          #pooja
#split
print(s.split(' '))         #['sh', 'n', 'y', '']
print(g.split(' '))         #['Pooja', 'anil', 'jagtap']
#strip
h=' top '
print(h.strip())            #'top'
#swapcase
print(g.swapcase())         #pOOJA ANIL JAGTAP
print(s.upper())            #SHANAYA
#find
print(g.find('anil'))        #6
print(g.find('shanaya'))    #-1
#index
print(g.index('anil'))       #6
#print('hi',g.index('shanaya'))  #it gives error, will not show '-1' as in find()

s1='counting {0} the {1} {2} string'
print(s1.format('substring','is','good')) #counting substring the is good string







print(bool(213))