def partition(arr, start, end):
    pivot_idx = (start + end) // 2
    arr[pivot_idx], arr[end] = arr[end], arr[pivot_idx]

    i = start

    #O(n)
    for j in range(start, end):
        if arr[j] <= arr[end]:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    
    arr[i], arr[end] = arr[end], arr[i]
    return i

def QuickSort(arr, start, end):
    if start >= end:
        return
    
    #O(logn) due to the tree of funtion calls
    pivot_idx = partition(arr, start, end)
    QuickSort(arr, start, pivot_idx - 1)
    QuickSort(arr, pivot_idx + 1, end)

arr = [1, -5, 10, 100, -4, 0, 3, 2, 1]
QuickSort(arr, 0, len(arr) - 1)
print(arr)