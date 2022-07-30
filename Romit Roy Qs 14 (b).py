#example 2
'''
***
**
*
#star 2 pattern 2
tr  r  nsp  nst
3   1  0    3
    2  0    2
    3  0    1
    tr ?    tr-r

'''
print ('pattern problem')
tr = int(input('enter the total no of rows'))

for r in range (tr):
    for nst in range (tr-r):
        print('*',end = ' ')
    print()
