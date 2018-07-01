
def getDigits(num):
    return [int(d) for d in str(num)]

def check_vampire_number(num):
    vampire_flag=False
    num_digits=getDigits(num)
    if(len(num_digits)%2==0):
        first_number=pow(10,len(num_digits)/2-1)
        while(first_number<=pow(10,len(num_digits)/2)/2):
            second_number=num/first_number
            first_number_digits=getDigits(first_number)
            second_number_digits=getDigits(second_number)
            if(sorted(num_digits)==sorted(first_number_digits+second_number_digits)):
                if(not(first_number%10==0 and second_number%10==0)):
                    vampire_flag=True
                    break;
            first_number+=1
    return vampire_flag


if __name__ == '__main__':
    print("Check for vampire number")
    num=126000
    vampire_flag=check_vampire_number(num)
    print(vampire_flag)