#Q.11)input two numbers and swap them using bitwise XOR operator  ??

x = int(input('enter a number'))
y = int(input('enter a number'))

x = x ^ y
y = x ^ y
x = x ^ y

print('value of x:',x)
print('value of y:',y)
