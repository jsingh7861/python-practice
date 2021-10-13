###
# Program to find the sum of square of first n natural number 
# Using mathematical formula
###

def sum_square(n): 
    if n < 0:
        print("Incorrect number")
    elif n == 0:
        print(n)
    elif n == 1:
        print(n)  
    else:
        sum = n * (n+1) * (2 * n + 1)//6
        print(sum)
if __name__ == "__main__":
    print("Enter the n number of which sum of squares need to be find")
    n = int(input())
    sum_square(n)