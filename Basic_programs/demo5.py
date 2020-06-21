###
#program to check whether number is armstrong or not
###

def arm_checker(num):
    if cubic_sum_finder(num) == num:
        print("Number is armstrong, number:", num)
    else:
        print("Number is not armstrong", num)


def cubic_sum_finder(num):
    cubic_sum = 0 
    while(num != 0):
        cubic_sum = cubic_sum + pow(int(num%10), 3)
        num = int(num/10)
    return cubic_sum 
    

if __name__ == "__main__":
    print("Enter the number to be checked for Armstrong or not:")
    num = int(input())
    cubic_sum_finder(num)
    arm_checker(num)

