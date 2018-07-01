def find_LIS_method_1(arr):
    # O(n^2) solution
    dp_table=[1 for x in range(len(arr))]
    result=0
    for i in range(1,len(arr)):
        for j in range(0,i):
            if(arr[i]>arr[j] and dp_table[i]<dp_table[j]+1):
                dp_table[i]=dp_table[j]+1

    return max(dp_table)


if __name__ == '__main__':
    print("To find the longest increasing subsequence")
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print (find_LIS_method_1(arr))
