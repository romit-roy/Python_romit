#example 6
'''
*****
 ***
  *

tr   r    nsp    nst
3    0    0      5
     1    1      3
     2    2      1
     tr   r      2*(tr-r)-1
'''

print ('pattern problem')
tr = int(input('enter the total no of rows'))

for r in range (tr):
    for nsp in range(r):
        print(' ',end =' ')
    for nst in range (2*(tr-r)-1):
        print('*',end = ' ')
    print()
