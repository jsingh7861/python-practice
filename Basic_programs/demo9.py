###
# python program for nth fibonacci number
###


## recursive approach 



def fibonacci_series(n):
    a = 0 
    b = 1
    if n < 0:
        print("Incorrrect number")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_series(n-1) + fibonacci_series(n-2)   

if __name__ == "__main__":
    print("nth number to print from Fibonacci series:")
    n = int(input())
    fibonacci_series(n)
    print(fibonacci_series(n))
