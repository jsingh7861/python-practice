

def prime_number(p,m):
    flag = True
    if (p == 0 or p == 1):
        print("It is not a prime number")
    elif(p>1):
        for i in range(2,m):     
            if (p%i == 0):
                print("It is not a prime number")
                flag = False 
                break 
    if flag == True:
        print(" It  is a prime number")
        


if __name__ == "__main__":
    print("Enter the number:")
    p = int(input())
    m = int(p/2)
    prime_number(p,m)