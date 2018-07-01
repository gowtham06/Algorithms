def find_longest_palindrome(srt):
    dp_table=[[0 for x in range(len(str))] for y in range(len(str))]
    for i in range(len(str)):
        dp_table[i][i]=1
    start_index=end_index=0
    max_length=0
    for i in range(len(str)-1):
        if(str[i]==str[i+1]):
            dp_table[i][i+1]=1
            max_length=2
            start_index=i
            end_index=i+1
    for i in range(3,len(str)+1):
        for j in range(0,len(str)-i+1):
            k=i+j-1

            if(dp_table[j+1][k-1]==1 and str[j]==str[k]):
                dp_table[j][k] = 1
                if(max_length<i):
                    max_length=i
                    start_index=j
                    end_index=k
                    max_length=i
    print(str[start_index:end_index+1])
    return max_length


if __name__ == '__main__':
    print("Longest Pallindrome")
    str='forgeeksskeegfor'
    print find_longest_palindrome(str)