#Q.29)take an array of decimal numbers and find their average

sum = 0
ListSum = [45,78,54,23,67]

for num in ListSum:
    sum = sum+num

avg = sum/len(ListSum)
print('sum of list elements is ',sum)
print('average of list elements is ',avg)
