#Q.26)input a number and check whether it is an krishnamurthy number or not using loop


num = int(input('enter a number:'))
tmp = num
s = 0
while num>0:
    r = num%10
    f = 1
    for i in range(1,r+1):
        f*=i
    s = s+f
    num//=10

if tmp == s:
    print('the number is krishnamurthy')
else:
    print('the number is not krishnamurthy')
