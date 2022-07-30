#Q.17)input a number and find its sum of digit

def getSum(n):


    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum


n = 12345
print(getSum(n))
