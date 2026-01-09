data =[1,2,3,4,5,6,7,8,9]

data=[x*2  for x in data ]

new_data =[x for x in data if x%4==0]

print("multiple by 2",data)

print ("divisible by 4",new_data)

str=["udaya krishnan","yo hi","la la"]



new_str= [x.replace(" ","_") for x in str]

print(new_str)