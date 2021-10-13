###
# Bubble sort program
# https://stackabuse.com/sorting-algorithms-in-python/
###


def bubble_sort(arr , n):
    swapped = True
    while swapped:
        swapped = False         
        for j in range(0,n-1):
            if arr[j] > arr[j+1]:
                swapped = True
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                
    print(arr)            

if __name__ == "__main__":
    arr = [3,5,6,2,8,2,1]
    n = len(arr)
    bubble_sort(arr , n)