#Q.9)input a number and find whether its prime or not  ??

num = int(input('enter a number'))
flag = False
if num > 1:
    for i in range (2, num):
        if (num % i)== 0:
            flag = True
            break
if flag:
    print (num ,"is not a prime number")
else:
    print (num ,"is a prime number")
