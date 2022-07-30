#Q.27)input a range (LL and UL)and find out the prime numbers within this range LL to UL

lower = int(input('enter a number'))
upper = int(input('enter a number'))

for num in range(lower,upper + 1):
    if num>1:
        for i in range (2,num):
            if(num%i)==0:
                break

        else:
            print(num)
