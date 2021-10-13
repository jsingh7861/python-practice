

def finder(array, search_this):
    decider = False
    for i in array:
        if i == search_this:
            decider = True
    if decider:
        print("Found:",search_this)
    else:
        print("Not found")


if __name__ == "__main__":
    x = [11,12,31,4,26,7,8,19,20]
    y = int(input("Enter the number to find in array:"))
    finder(x, y)