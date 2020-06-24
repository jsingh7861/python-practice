###
# program to print all the prime number in given interval
# In most of the programming languages (C/C++, Java, etc), 
# the use of else statement has been restricted with the if conditional statements. 
# But Python also allows us to use the else condition with for loops. 
# The else block just after for/while is executed only 
# when the loop is NOT terminated by a break statement.
###

#def prime_num_finder():
#    for num in range(2, 100):
#       if num % 2 != 0:
#            print(num, "is a prime number")

def prime_num_finder(low_num , high_num):
    for num in range(low_num , high_num + 1):
        if num > 0:
            for i in range(2 , num):
                if num % i == 0:
                    break
            else:
                print(num)    
       
if __name__ == "__main__":
    print("Enter the lowest number:")
    low_num = int(input())
    print("Enter the highest number:")
    high_num = int(input())
    prime_num_finder(low_num , high_num)


            
