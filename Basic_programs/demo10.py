###
# program to print n number of fibonaci numbers

##

def fibonacci_series(n):
    n1 = 0 
    n2 = 1
    count = 0
    if n < 0:
        print("Please enter valid number")
    elif n == 1:
        print(n2)    
    else:
        print("fibonacci series:")
        while count < n:
            print(n1)
            sum = n1 + n2
            n1 = n2
            n2 = sum 
            count += 1


if __name__ == "__main__":
    print("How many fibonacci numbers?")
    n = int(input())
    fibonacci_series(n)
