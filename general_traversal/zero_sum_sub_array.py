def check_for_zero_sum(arr):
    hash_map=[]
    sum_so_for=0
    check_flag=False
    for i in range(len(arr)):
        sum_so_for+=arr[i]
        if sum_so_for in hash_map or sum_so_for==0:
            check_flag=True
            break
        else:
            hash_map.append(sum_so_for)
    return check_flag
if __name__ == '__main__':
    print("Zero sub array sum")
    num_arr=[1,2,3,4,5,-15]
    check_flag=check_for_zero_sum(num_arr)
    print(check_flag)