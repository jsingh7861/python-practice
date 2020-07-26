###
# Program to find the sum of square of first n natural number 
###

def sum_square(n): 
    if n < 0:
        print("Incorrect number")
    elif n == 0:
        print(n)
    elif n == 1:
        print(n)  
    else:
        sum = 0       
        for i in range(1,n+1):
            sum = sum + (i * i)
        print(sum)
if __name__ == "__main__":
    print("Enter the n number of which sum of squares need to be find")
    n = int(input())
    sum_square(n)