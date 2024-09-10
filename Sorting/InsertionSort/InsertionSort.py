def InsertionSort(arr: list):
    for i in range(len(arr)):
        j = i

        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

    return arr

sorted = InsertionSort([1, -5, 10, 100, -4, 0, 3, 2, 1])
print(sorted)