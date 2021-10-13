
def search_number(a):
    search_this = int(input("Number to find:"))
    finder = False
    for i in a:
        if i == search_this:
            finder = True
            print(i)
            break
    if finder:
        print("Number found:",search_this) 
    else:
        print("Number not found")       
## Time complexity= BIG_O(size_of_array)
## If we are not using break , loop is going to check each element 
## Let's say if we are inputting 10 element , time complexity will become O(10)
## By using break it will become O(number at which element is found)

def input_taker():
    x = []
    size = int(input("How many elements in array/List:"))
    for i in range(0,size):
        element = int(input())
        x.append(element)
    print(x)    
    search_number(x)




if __name__ == "__main__":
    input_taker()