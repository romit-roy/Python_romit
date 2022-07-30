#example 1
'''
*
**
***
#star 1 pattern 1
tr  r  nsp  nst
3   1  0    1
    2  0    2
    3  0    3
    tr ?    r
'''
print ('pattern problem')
tr = int(input('enter the total no of rows'))

for r in range (tr):
    for nst in range (r):
        print('*',end = ' ')
    print()
