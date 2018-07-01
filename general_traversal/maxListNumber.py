import functools
def comparator_function(value_1,value_2):
    comb_12=int(str(value_1)+str(value_2))
    comb_21 =int(str(value_2) + str(value_1))
    if comb_12<comb_21:
        return -1
    elif comb_12>comb_21:
        return 1
    else:
        return 0

def find_max(num_arr):
    sorted_arr=sorted(num_arr,key=functools.cmp_to_key(comparator_function),reverse=True)
    return ''.join(str(item) for item in sorted_arr)

if __name__ == '__main__':
    print("Finding the maximum number from a given list of numbers")
    num_arr=[1,2,2,4,10,9,85]
    print(find_max(num_arr))
