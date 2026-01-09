list=[1,2,3,4,5]



list.append(6) # to adding one value

list.extend([2,8,9,11])# to adding multiple value

# list.pop(2)# reomoving the index value

list.remove(11)# removing the exact value 
# list.clear()# clear the list
list_copy=list.copy()

count_list=list.count(2)# counting the exact value

print(count_list)
print(list_copy)
print(list)