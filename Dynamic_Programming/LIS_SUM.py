def find_LIS_sum(arr):
    dp_table=[0 for i in range(len(arr))]
    dp_table[0]=arr[0]
    for i in range(1,len(arr)):
        for j in range(0,i):
            if(arr[j]<arr[i] and dp_table[i]<dp_table[j]+arr[i]):
                dp_table[i]=dp_table[j]+arr[i]
    return max(dp_table)
if __name__ == '__main__':
    print("To find the longest increasing sequence sum in a given array")
    arr=[3, 4, 5, 1]
    print(find_LIS_sum(arr))