# QuickSort Algorithm

## Introduction

Quicksort is a highly efficient sorting algorithm and is based on the divide-and-conquer approach. Developed by Tony Hoare in 1960, it is widely used due to its average-case efficiency and simplicity in implementation.

## How QuickSort Works

Quicksort works by selecting a **pivot** element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

### Steps:

1. **Choose a pivot** element from the array.
2. **Partition**: Rearrange the elements of the array so that all elements less than the pivot come before it, and all elements greater come after it.
3. **Recursion**: Recursively apply the same process to the sub-arrays of elements less than and greater than the pivot.

### Base Case:

The recursion terminates when the sub-array has only one or zero elements, which is inherently sorted.

### Example:

Array: [3, 6, 8, 10, 1, 2, 1]

1.  Choose pivot (e.g., 1)
2.  Partition: [1, 1, 2, 3, 6, 8, 10]
3.  Recursively sort the partitions

## Algorithm Performance

- **Best Case Time Complexity**: O(n log n)
  This occurs when the pivot divides the array into two nearly equal parts.
- **Average Case Time Complexity**: O(n log n)
  The average case occurs when the pivot roughly divides the array in half each time.
- **Worst Case Time Complexity**: O(n²)
  This happens when the pivot is always the smallest or largest element, resulting in an unbalanced partition (e.g., sorted or reverse-sorted input).
- **Space Complexity**: O(log n)
  The space complexity is due to the recursion stack in the worst case, and it's optimized in in-place implementations.

## Key Concepts

- **Pivot Selection**: A bad choice of pivot (e.g., always choosing the first element) can lead to poor performance. Randomized pivot selection or median-of-three approaches can improve average performance.
- **In-Place Sorting**: Quicksort can be implemented in-place, requiring no extra storage space beyond the recursion stack.

- **Not Stable**: Quicksort is not a stable sort, meaning that it may change the relative order of equal elements.

## Pros and Cons

### Pros:

- **Fast**: Average-case time complexity of O(n log n).
- **In-Place Sorting**: Requires minimal extra memory.
- **Widely Used**: Suitable for large datasets.

### Cons:

- **Worst Case**: Time complexity can degrade to O(n²) with poor pivot choices.
- **Not Stable**: Can change the relative order of equal elements.

## Applications

- **General-purpose sorting**: Suitable for most general sorting tasks.
- **Used in libraries**: Many languages' standard sorting libraries use quicksort or its variants (e.g., Python's `sorted()` uses Timsort, which is a hybrid algorithm with quicksort characteristics).
