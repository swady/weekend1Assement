print('Enter the triangle lenths:')
x=int(input(' enter side one:'))
y=int(input(' enter side two:'))
z=int(input(' enter side three:'))
if x==y==z :
    print('Triangle is equailateral')
elif x==y or x==z or y==z :
    print('Traiangle is isoscales')
else:
    print('Traiangle is scalene')
