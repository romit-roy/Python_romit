#Q.8)input three numbers and find the largest and smallest number
#largest number

a = int(input('enter a number'))
b = int(input('enter a number'))
c = int(input('enter a number'))
if a>b and a>c:
    print(a ,"a is largest")
elif b>a and b>c :
    print(b ,"b is largest")
else:
    print(c ,"c is largest")

#smallest number

a = int(input('enter a number'))
b = int(input('enter a number'))
c = int(input('enter a number'))
if a<b and a<c:
    print(a ,"a is smallest")
elif b<a and b<c :
    print(b ,"b is smallest")
else:
    print(c ,"c is smallest")
