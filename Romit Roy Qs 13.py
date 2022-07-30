#Q.13)input a decimal number nad finds its octal using array

def decToOctal(n):
    octalnum = [0]*100
    i = 0
    while (n!= 0):
        octalnum[i] = n%8
        n = int(n/8)
        i+= 1
    for j in range(i - 1, -1 , -1):
        print(octalnum[j],end = " ")
n = 33
decToOctal(n)
