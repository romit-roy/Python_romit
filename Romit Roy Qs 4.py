#Q.4)input two numbers and swap them using third variable , and without using third variable  ??

x = int(input('enter a number'))
y = int(input('enter a number'))
temp = x
x = y
y = temp

print('the value of x after swapping: {}'.format(x))
print('the value of y after swapping: {}'.format(y))
