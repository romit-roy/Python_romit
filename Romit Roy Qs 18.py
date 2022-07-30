#Q.18)input a number and find its reverse

num = int(input('enter a number:'))
reversed_num = 0

while num!=0:
    digit = num%10
    reversed_num = reversed_num*10+digit
    num//= 10

print('reversed number:' +str(reversed_num))
