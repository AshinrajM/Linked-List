# Binary Search is a search with O(log n) time complexity but the array has to be in sorted order

def BinarySearch(arr,value):
    start=0
    end=len(arr)-1
    mid=(start+end)//2
    while start<=end:
        if value==arr[mid]:
            return mid
        elif value <arr[mid]:
            end=mid-1
            mid=(start+end)//2

        else:
            start=mid+1
            mid=(start+end)//2
    return "not found"

arr=[1,2,3,4,5,6,7,8,9]
print(BinarySearch(arr,13))


# Recursive Binary Search


def RecursiveBinarySearch(arr, value, start=0, end=None):
    
    if end is None:
        end=len(arr)-1
    
    if start<=end:
        mid=(start+end)//2

        if arr[mid]==value:
            return mid

        elif value < arr[mid]:                                                                   
            end = mid-1
            return RecursiveBinarySearch(arr,value,start,end)
        else:
            start=mid+1
            return RecursiveBinarySearch(arr,value,start,end)
    else:
        return "Not Found"



arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(RecursiveBinarySearch(arr, 11))


Linear search

def LinearSearch(value,arr):
    for i in range(len(arr)):
        if value==arr[i]:
            return i
    return "not found"

arr=[1,2,3,4,5,6,7,8,9,13]
print(BinarySearch(arr,13))
