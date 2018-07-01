def required_sortin(num_arr):
    counter=0
    mid=0
    end=len(num_arr)-1
    start=0
    pivot=1
    while(mid<=end):
        if(num_arr[mid]<pivot):
            num_arr[mid],num_arr[start]=num_arr[start],num_arr[mid]
            mid+=1
            start+=1
        elif(num_arr[mid]>pivot):
            num_arr[mid],num_arr[end]=num_arr[end],num_arr[mid]
            # mid+=1
            end-=1
        else:
            mid+=1
if __name__ == '__main__':
    print("In dutch flag sorting")
    num_arr=[0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0 ]
    required_sortin(num_arr)
    print(num_arr)
