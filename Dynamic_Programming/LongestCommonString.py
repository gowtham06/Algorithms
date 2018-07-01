def find_lcs_String(str_1,str_2):
    dp_table=[[0 for y in range(len(str_1)+1)] for x in range(len(str_2)+1)]
    # print dp_table
    common_string_max_length=0
    start=end=0
    for x in range(len(str_2)+1):
        for y in range(len(str_1)+1):
            if(x==0 or y==0):
                dp_table[x][y]=0
            elif(str_2[x-1]==str_1[y-1]):
                dp_table[x][y]=dp_table[x-1][y-1]+1
                if(common_string_max_length<dp_table[x][y]):
                    start=x
                    end=y
                    common_string_max_length=dp_table[x][y]

    result_string=['' for x in range(common_string_max_length)]
    pos=common_string_max_length-1
    while(dp_table[start][end]!=0):
        result_string[pos]=str_2[start-1]
        start=start-1
        end=end-1
        pos=pos-1
    return ''.join(result_string)

if __name__ == '__main__':
    print("In longest common sub string module")
    str_1= 'geeksforaageeks'
    str_2 = 'aageeksquiz'
    print (find_lcs_String(str_1,str_2))