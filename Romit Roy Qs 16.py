#Q.16)input a number and find their HCF nad LCM without using Euclidians theoram

#HCF

a = int(input('enter a first number'))
b = int(input('enter a second number'))

HCF = 1

for i in range(2,a+1):
    if(a%i==0 and b%i==0):
        HCF = i

print('first number is :',a)
print('second number is :',b)
print('HCF of the numbers is :',HCF)


#LCM

a = int(input('enter a first number'))
b = int(input('enter a second number'))

HCF = 1

for i in range(2,a+1):
    if(a%i==0 and b%i==0):
        HCF = i

print('first number is :',a)
print('second number is :',b)

LCM = int((a*b)/(HCF))
print('LCM of the two numbers is :',LCM)
