#example 4
'''
***
 **
  *
#star 4 pattern 4

tr  r  nsp    nst
3   0  0      3
    1  1      2
    2  2      1
    tr r      tr-r
'''
print ('pattern problem')
tr = int(input('enter the total no of rows'))

for r in range (tr):
    for nsp in range(r):
        print(' ',end =' ')
    for nst in range (tr-r):
        print('*',end = ' ')
    print()
