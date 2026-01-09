def  sum_of(**kwargs) :
    sum=0
    for x,v in kwargs.items():
        sum+=v
    return sum

print(sum_of(coffee= 20, cake=100,juice=50))