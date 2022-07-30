#Q.28)input a number and print all twin prime numbers up to that number

def is_prime(n):
    for i in range (2 , n):
        if n % i == 0:
            return False
        return True

def generate_twins(start,end):
    for i in range(start,end):
        j = i + 2
        if (is_prime(i) and is_prime(j)):
            print('{:d} and {:d}'.format (i , j))


generate_twins(2, 100)
