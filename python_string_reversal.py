# str[start:stop:step]

str="reversal"

# reverse=str[::-1]

# print(reverse)


def reverse_string(str):
    if len(str)==0 :
        return str
    else :
        return reverse_string(str[1:])+str[0]
    

print(reverse_string(str))