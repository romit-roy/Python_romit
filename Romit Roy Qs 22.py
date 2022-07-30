#Q.22)input a number and finds its factor

def print_factors (x):
    print('the factors of ',x,'are:')
    for i in range (1 , x+1):
        if x % i == 0:
            print(i)


num = int(input('enetr a number'))

print_factors(num)
