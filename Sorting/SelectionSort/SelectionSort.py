def SelectionSort(arr: list):
    for i in range(len(arr) - 1):
        min_idx = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

sorted = SelectionSort([45, 100, 0, 1, -5, -10, 4, 5, 6, 13])
print(sorted)