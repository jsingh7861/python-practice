###
# program to print the armstrong number between 0 and 999
###



def armstrong_num():
    for num in range(10, 100000):
        temp = num
        sum = 0
        while num > 0:
            sum = sum + pow(num%10, 3)
            num = int(num/10)
        cubic_sum = sum    
        if temp == cubic_sum:
            print("Armstrong number", temp)   


if __name__ == "__main__":
    armstrong_num()