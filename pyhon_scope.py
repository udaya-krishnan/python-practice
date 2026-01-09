#globle scope

# print("accessing globle veriable before declering ", my_globle) this is not possible showing name error

my_globle=10

def fn1():
    my_fn1=20
    print("Access Globl veriable",my_globle)
    print("Accessing veriable on the function",my_fn1)
    # print("Accessing veriable another fuction ",my_fn2) Its not possible 
    
    def fn2 ():
        my_fn2=30
        print("Accessing myfn1 veriable",my_fn1)
        print("Accessing Globle veriable",my_globle)
    fn2()
        


fn1()

# print("Accessing the verable oute side the function",my_fn1) showing Name error

