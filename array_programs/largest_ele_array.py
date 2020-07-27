###
# Program to find the largest element in an array
###


def largest_element(arr , n):
    max = arr[0]
    for i in range(1 , n):
        if arr[i] > max:
            max = arr[i]
    print(max)        

if __name__ == "__main__":
    print("Enter the array")
    arr = [5,10,20,1,0,7,80,90]
    n = len(arr)
    largest_element(arr , n)