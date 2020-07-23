###
# Finding fibonacci number using dynamic programming
###

    



def fibonacci_finder(n):
    fib_array  = [0,1]
    if n < 0:
        print("Incorrect number")
    elif n <= len(fib_array):
        return fib_array[n-1] 
    else:
        fib = fibonacci_finder(n-1) + fibonacci_finder(n-2)
        fib_array.append(fib)
        return fib


if __name__ == "__main__":
    print("Enter the nth number for fibonacci")
    n = int(input())
    print(fibonacci_finder(n))