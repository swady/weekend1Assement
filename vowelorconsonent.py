x= raw_input('Enter a alphabet :')
y= ('a','e','i','o','u')
if  x in y:
    print( x,'is vowel')
else:
    print(x,'is consonent')

    
#My updated
if x in 'aeiouAEIOU':
    print(x+'is a vovel')
else:
    print(x+'is a consonant')
