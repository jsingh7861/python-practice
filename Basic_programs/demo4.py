###
# Program to calculate the compound interest
###
def compound_interest(p, r , t):
    ci = p * (pow((1+ r/100), t))
    print("Compund interst for years is", ci)


if __name__ == "__main__":
    print("Enter the principle amount:")
    p = int(input())
    print("Enter the rate of interest:")
    r = int(input())
    print("Enter the time period in years:")
    t = int(input())
    compound_interest(p, r, t)
