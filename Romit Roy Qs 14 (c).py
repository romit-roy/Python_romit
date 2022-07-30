#example 3
'''
  *
 **
***
#star 3 pattern 3

tr   r   nsp     nst
3    0   2       1
     1   1       2
     2   0       3
     tr  tr-r-1  r+1
'''
print ('pattern problem')
tr = int(input('enter the total no of rows'))

for r in range (tr):
    for nsp in range(tr-r-1):
        print(' ',end =' ')
    for nst in range (r+1):
        print('*',end = ' ')
    print()
