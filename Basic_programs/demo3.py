###
#Program to caclcualte the simple interest
###

def simple_interest(p, r, t):
    print((p*r*t)/100)

if __name__ == "__main__":
    print("Enter the principal amount:")
    p = int(input())
    print("Enter the rate of interest:")
    r = int(input())
    print("Enter the time:")
    t = int(input())
    simple_interest(p, r, t)