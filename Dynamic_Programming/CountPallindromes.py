
def count_pallidromes(str_1):
    # n=len(str_1)
    dp_table = [[0 for y in range(len(str_1) + 1)] for x in range(len(str_1) + 1)]
    bool_table=[[False for y in range(len(str_1) + 1)] for x in range(len(str_1) + 1)]
    for i in range(len(str_1)):
        bool_table[i][i]=True
    i=0
    while(i<len(str_1)-1):
        if(str_1[i]==str_1[i+1]):
            bool_table[i][i+1]=True
            dp_table[i][i+1]=1
        i=i+1
    for i in range(2,len(str_1)):
        for j in range(0,len(str_1)-i):
            k=i+j
            if(str_1[j]==str_1[k] and bool_table[j+1][k-1]):
                bool_table[j][k]=True
            if(bool_table[j][k]==True):
                dp_table[j][k]=dp_table[j][k-1]+dp_table[j+1][k]-dp_table[j+1][k-1]
            else:
                dp_table[j][k]=dp_table[j][k-1]+dp_table[j+1][k]-dp_table[j+1][k-1]
    return dp_table[0][len(str_1)-1]
if __name__ == '__main__':
    str_1="abaab"
    print(count_pallidromes(str_1))

