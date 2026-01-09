my_list=[1,2,3]

def adding_value (my_list):

    copy_mylist=my_list.copy()
    copy_mylist.append(4)
    return copy_mylist

print(adding_value(my_list))
print(my_list)