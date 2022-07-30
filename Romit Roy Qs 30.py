#Q.30)take an array of decimal numbers and delete the repetitive occurrences of the element from the array 

sam_list = [11,13,15,16,13,15,16,11]
print(' the list is :' +str(sam_list))
result = []
for i in sam_list:
    if i not in result :
        result.append(i)

print('the list after deleteing repetitive:'+str(result))
