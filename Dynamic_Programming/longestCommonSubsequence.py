def find_LCS(str_1,str_2):
    dp_table=[[0 for y in range(len(str_2)+1)] for x in range(len(str_2)+1)]
    result=0
    for i in range(len(str_1)+1):
        for j in range(len(str_2)+1):
            if(i==0 or j==0):
                dp_table[i][j]=0
            elif(str_1[i-1]==str_2[j-1]):
                dp_table[i][j]=dp_table[i-1][j-1]+1
            else:
                dp_table[i][j]=max(dp_table[i-1][j],dp_table[i][j-1])

    # return dp_table[len(str_1)][len(str_2)]
    lcs_string=''
    i=len(str_1)
    j=len(str_2)
    while(i>=0 and j>=0):
        if(str_1[i-1]==str_2[j-1]):
            lcs_string=str_1[i-1]+lcs_string
            i=i-1
            j=j-1
        elif(dp_table[i-1][j]>dp_table[i][j-1]):
            i=i-1
        else:
            j=j-1
    return lcs_string


if __name__ == '__main__':
    print("To find the longest common sub string")
    str_1 = 'AGGTAB'
    str_2= 'GXTXAYB'
    print (find_LCS(str_1,str_2))