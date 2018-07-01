def generate_strings(final_string,index,string_1,string_2,len_1,len_2):
    if(len_1==0 and len_2==0):
        print final_string
    if(len_1!=0):
        final_string[index]=string_1[0]
        generate_strings(final_string,index+1,string_1[1:],string_2,len_1-1,len_2)
    if (len_2 != 0):
        final_string[index] = string_2[0]
        generate_strings(final_string, index + 1, string_1, string_2[1:], len_1, len_2-1)
    


if __name__ == '__main__':
    print("Interveing Strings")
    string_1='ABC'
    string_2='DEF'
    final_string=['']*(len(string_1)+len(string_2))
    # print(final_string)
    generate_strings(final_string,0,string_1,string_2,len(string_1),len(string_2))