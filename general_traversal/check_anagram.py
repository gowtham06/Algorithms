def check_anagram(str_1,str_2):
    str_1_key_set=set(str_1.split())
    str_2_key_set=set(str_2.split())
    return str_1_key_set==str_2_key_set
if __name__=='__main__':
    print("Check_Anagran")
    str_1="abcdefgh"
    str_2="zxcabcdefg"
    print(check_anagram(str_1,str_2))