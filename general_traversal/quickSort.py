def quick_sort(num_arr):
    if not num_arr:
        return []
    lesser=quick_sort([item for item in num_arr if  item<num_arr[0]])
    pivots=[item for item in num_arr if item==num_arr[0]]
    greater=quick_sort([item for item in num_arr if item>num_arr[0]])
    return lesser+pivots+greater
if __name__ == '__main__':
    print("Quick sort module")
    num_arr=[9,2,1,4,6,0,0,3,8]
    num_arr=quick_sort(num_arr)
    print(num_arr)
