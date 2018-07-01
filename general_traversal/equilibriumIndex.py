def find_equilibrium_index(num_arr):
    find_flg=False
    req_index=-1
    left_sum=[0]*len(num_arr)
    for i in range(1,len(num_arr)-1):
        left_sum[i]=left_sum[i-1]+num_arr[i-1]
    right_sum=0
    for j in range(len(num_arr)-1,-1,-1):
        if(right_sum==left_sum[j]):
            find_flg=True
            req_index=j
            break;
        else:
            right_sum+=num_arr[j]
    return req_index

if __name__ == '__main__':
    print("Finding the equilibrium index")
    num_arr=[0,-3,5,-4,-2,3,1,10]
    print(find_equilibrium_index(num_arr))