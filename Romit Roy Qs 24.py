#Q.24)input a number and check whether it is an automorphic number or not using loop

print('enter a number:')
n = int(input())
sq = n*n
co = 0
while(n>0):
    if(n%10!=sq%10):
        print('not automorphic')
        co = 1
        break
    n = n//10
    sq=sq//10

if(co==0):
    print('automorphic')
