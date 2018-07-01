import math
def find_rank(str):
    sorted_charactes=sorted(str)
    # print(sorted_charactes)
    counter=0
    for index,item in enumerate(str):
        pos=sorted_charactes.index(item)
        possible_characters=sorted_charactes[:pos]
        counter+=len(possible_characters)*math.factorial(len(str)-1-index)
        # print(item,len(str)-1-index),
        # print(item,len(possible_characters))
        sorted_charactes.remove(item)
        # print(item,len(possible_characters)*math.factorial(len(str)-1-index))
    return counter+1
if __name__ == '__main__':
    print("To find the rank of a string")
    str_1="string"
    print(find_rank(str_1))

