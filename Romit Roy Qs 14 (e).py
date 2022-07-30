#example 5
'''
  *
 ***
*****
tr   r   nsp     nst
3    0   2       1
     1   1       3
     2   0       5
     tr  tr-r-1  2*r+1
'''
print ('pattern problem')
tr = int(input('enter the total no of rows'))

for r in range (tr):
    for nsp in range(tr-r-1):
        print(' ',end =' ')
    for nst in range (2*r+1):
        print('*',end = ' ')
    print()
