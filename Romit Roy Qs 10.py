#Q.10)solve a given quadratic equation [without imaginary roots]  ??

import cmath

a = int(input('enter a number'))
b = int(input('enter b number'))
c = int(input('enter c number'))

d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('the solution are {0} and {1} '.format(sol1,sol2))
