def generate_n_gram(string,n):
    n_gram_list=[]
    split_string=string.split(' ')
    for i in range(0,len(split_string)-n+1):
        str=''
        for j in range(i,i+n):
            str=str+' '+split_string[j]
        n_gram_list.append(str)

    # print(n_gram_list)
    return n_gram_list
if __name__ == '__main__':
    print("To generate N-Grams")
    string="My name is Gowtham Kannan"
    print(generate_n_gram(string,4))