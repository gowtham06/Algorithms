permutation_list=[]
def generate_permute(string_list,left,right):
    if(left==right):
        # print ''.join(string_list)
        permutation_list.append(''.join(string_list))
        # print("Generate")
        # print("left={value_2},right={value_3}").format(value_2=left, value_3=right)

    else:
        for i in range(left,right+1):
            # print("i={value_1},left={value_2},right={value_3}").format(value_1=i,value_2=left,value_3=right)

            string_list[i],string_list[left]=string_list[left],string_list[i]
            generate_permute(string_list,left+1,right)
            string_list[left],string_list[i]=string_list[i],string_list[left]

if __name__ == '__main__':
    print("To generate permutations of a string")
    str_1="abcd"
    generate_permute(list(str_1),0,len(str_1)-1)
    print(permutation_list)
    # print(len(permutation_list))
    item_list=[('a',0),('b',1),('c',2)]
    tuple_item=item_list.pop()
    print(tuple_item)