def main():
    sum=0
    number = [5,6,7,14,152,60693]
    for i in range(100):
        sum+=i+1
        if(i>=5 and i <=8):
            azeret_num=azerer(i)
            print(azeret_num)
        if (i<6):
            num_prime=is_prime(number[i])
            print(num_prime)
    
def azerer(num):
    azeret_sum=1
    for i in range(num):
        azeret_sum*=i+1
    return azeret_sum


def is_prime(number_prime):
    
        print(number_prime)
        for i in range(2,number_prime-1):
            if (number_prime%i==0):
                return False
        return True

if (__name__ == "__main__"):
    main()

