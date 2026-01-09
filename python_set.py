# set is build-in data structure only store unique values also set not like list we can't get the index

set_a={1,2,3,4,5}

set_b={4,5,6,7,8}


print(set_a.union(set_b)) # or set_a | set_b  joining both set 
print(set_a.intersection(set_b)) # or set_a& set_b  get the match value eg: 4 ,5
print(set_a.difference(set_b)) # or  set_a- set_b get all the elements in set a but not in the set b eg:1,2,3
print(set_a.symmetric_difference(set_b)) # or set_a ^ set_b all the elements present in set a or set b but not in both sets
