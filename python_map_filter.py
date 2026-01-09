menu=["biriyani","mandhi","porotta","chapathi"]


def find_mandhi(mandi) :
    if mandi[0]=="m" :
        return mandi
    

map_mandhi=map(find_mandhi,menu)

for x in map_mandhi :
    print(x)


filter_mandhi=filter(find_mandhi,menu)

for x in filter_mandhi :
    print(x)