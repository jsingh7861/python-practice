###
#program to print all the prime number in given interval
###

#def prime_num_finder():
#    for num in range(2, 100):
#       if num % 2 != 0:
#            print(num, "is a prime number")

        
#if __name__ == "__main__":
#    prime_num_finder()


low_num = int(input())
high_num = int(input())
for num in range(low_num, high_num + 1):
    if num > 0:
        for i in range(2 , num):
            if num % i == 0:
                break
        else:
            print(num)

            
