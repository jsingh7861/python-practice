###
# Python program to calculate the sum of cubes using improved mathematical equation
###

def sum_cube(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2 == 0:
        sum = n/2 * (n+1)    
    else:
        sum = ((n + 1) / 2) * n  
    return (sum * sum)       

if __name__ == "__main__":
    print("Enter the n number of which sum of cubes need to be find")
    n = int(input())
    print(sum_cube(n))