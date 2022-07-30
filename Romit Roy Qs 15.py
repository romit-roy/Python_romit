#Q.15)input a number and find their HCF nad LCM using Euclidians theora

#using Euclidian
def computer_hcf(x,y):
    while(y):
        x,y=y,x%y
    return x

hcf = computer_hcf(300,400)
print('the HCF is',hcf)
