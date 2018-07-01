def find_mean(arr_1,arr_2):
    if(len(arr_1)==len(arr_2)==0):
        return float(-1)
    elif(len(arr_1)==len(arr_2)==1):
        return (arr_1[0]+arr_2[0])/2
    elif(len(arr_1)==len(arr_2)==2):
        return (max(arr_1[0],arr_2[0])+min(arr_1[1],arr_2[1]))/2
    else:
        median_1=median_2=0.0
        if(len(arr_1)%2==0):
            median_1=(arr_1[len(arr_1)/2]+arr_1[(len(arr_1)/2)+1])/2
        else:
            median_1=arr_1[(len(arr_1)+1)/2]
        if (len(arr_2) % 2 == 0):
            median_2 = (arr_2[len(arr_2) / 2] + arr_2[(len(arr_2) / 2) + 1]) / 2
        else:
            median_2 = arr_2[(len(arr_2) + 1) / 2]

        if(median_1==median_2):
            return median_1
        elif(median_1>median_2):
            arr_1=arr_1[0:(int(len(arr_1)/2))+1]
            arr_2=arr_2[int(len(arr_2)/2):]
            return find_mean(arr_1,arr_2)
        else:
            arr_2 = arr_2[0:(int(len(arr_2) / 2)) + 1]
            arr_1 = arr_1[int(len(arr_1) / 2):]
            return find_mean(arr_1, arr_2)




if __name__ == '__main__':
    print "To find the median between two arrays"
    arr_1=[1, 12, 15, 26, 38]
    arr_2=[2, 13, 17, 30, 45]
    print find_mean(arr_1,arr_2)