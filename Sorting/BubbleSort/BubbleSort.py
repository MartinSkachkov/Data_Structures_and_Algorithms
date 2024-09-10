def BubbleSort(arr: list):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

sorted = BubbleSort([1, -5, 0, 2, -1, 10, 9, 100, 56, -34])
print(sorted)