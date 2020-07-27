###
# Bubble sort program
###


def bubble_sort(arr , n):
    for i in range(n-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    print(arr)            

if __name__ == "__main__":
    arr = [3,5,6,2,8,2,1]
    n = len(arr)
    bubble_sort(arr , n)