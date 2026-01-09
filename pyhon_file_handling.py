# file = open("text.txt",mode="r")

# data= file.readline()

# print(data)

# file.close()


with open("text.txt", mode="r") as file :
    data=file.readline()
    print(data)


with open("index.txt",mode="r") as file :
    data=file.readlines()
    print(data)

