#Q.21)input a number and find its factorial

num = int(input('enter a number'))

factorial = 1
if num < 0:
    print ('Sorry,factorial does not exist for negative numbers')
elif num == 0:
    print('the factorial of 0 is 1')
else:
    for i in range (1, num+1):
        factorial = factorial*i
    print('the factorial of ',num , 'is', factorial) 
