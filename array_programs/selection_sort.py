###
# Selection sort algo 
#The selection sort algorithm sorts an array by repeatedly finding the minimum element 
#(considering ascending order) from unsorted part and putting it at the beginning. 
#The algorithm maintains two subarrays in a given array.
#1) The subarray which is already sorted.
#2) Remaining subarray which is unsorted.
###

def selection_sort(arr , n):
    for i in range(n):
        minpos = i
        for j in range(i,n):
            if arr[j] < arr[minpos]:
                minpos = j
        temp = arr[i]
        arr[i] =  arr[minpos]
        arr[minpos] = temp
    print(arr)

if __name__ == "__main__":
    arr = [64,25,12,22,11,16]
    n = len(arr)
    selection_sort(arr , n )