def MergeSort(arr):
    #define base case: array with single item by default is sorted
    if len(arr) == 1:
        return
    
    #divide phase
    middle_index = len(arr) // 2
    left_half = arr[:middle_index]
    right_half = arr[middle_index:]

    MergeSort(left_half)
    MergeSort(right_half)

    #conquer phase
    l = 0
    r = 0
    m = 0

    while l < len(left_half) and r < len(right_half):
        if left_half[l] < right_half[r]:
            arr[m] = left_half[l]
            m += 1
            l += 1
        else:
            arr[m] = right_half[r]
            m += 1
            r += 1

    #additional items in left or right half
    while l < len(left_half):
        arr[m] = left_half[l]
        m += 1
        l += 1

    while r < len(right_half):
        arr[m] = right_half[r]
        m += 1
        r += 1

arr = [1, -5, 10, 100, -4, 0, 3, 2, 1]
MergeSort(arr)
print(arr)