###
# Python program to calculate the sum of cubes 
###

def sum_cube(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        sum = (n * (n + 1) / 2)   
        return (sum * sum)       

if __name__ == "__main__":
    print("Enter the n number of which sum of cubes need to be find")
    n = int(input())
    print(sum_cube(n))