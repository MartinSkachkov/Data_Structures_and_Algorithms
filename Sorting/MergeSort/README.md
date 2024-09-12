# MergeSort Algorithm

## Introduction

MergeSort is a popular sorting algorithm that follows the divide-and-conquer approach. It was invented by John von Neumann in 1945 and is known for its consistent O(n log n) performance in all cases. Unlike QuickSort, MergeSort guarantees stability and is particularly useful for sorting linked lists or datasets too large to fit into memory.

## How MergeSort Works

MergeSort divides the array into two halves, recursively sorts each half, and then merges the two sorted halves back together. The merging process ensures the final array is sorted.

### Steps:

1. **Divide** the array into two halves.
2. **Recursively sort** each half.
3. **Merge** the two sorted halves into one sorted array.

### Base Case:

The recursion terminates when a sub-array contains only one element (or is empty), which is inherently sorted.

### Example:

Array: [38, 27, 43, 3, 9, 82, 10]

1.  Divide: [38, 27, 43] and [3, 9, 82, 10]
2.  Recursively sort each half [38, 27, 43] -> [27, 38, 43] [3, 9, 82, 10] -> [3, 9, 10, 82]
3.  Merge sorted halves [27, 38, 43] and [3, 9, 10, 82] -> [3, 9, 10, 27, 38, 43, 82]

## Algorithm Performance

- **Best Case Time Complexity**: O(n log n)
- **Average Case Time Complexity**: O(n log n)
- **Worst Case Time Complexity**: O(n log n)
  - MergeSort always has the same time complexity, regardless of the input's order.
- **Space Complexity**: O(n)
  - MergeSort requires additional memory space for the temporary arrays used in the merging process.

## Key Concepts

- **Stable Sorting**: MergeSort is a stable sort, meaning that it preserves the relative order of equal elements, making it ideal when the stability of the sort is required.
- **Divide and Conquer**: The array is divided into smaller arrays until each contains one element, which is then merged together in sorted order.

- **Suitable for Linked Lists**: MergeSort performs particularly well with linked lists, where its space complexity can be reduced to O(1) as merging does not require additional memory.

- **Not In-Place**: MergeSort requires additional space proportional to the size of the input array for the merge operation.

## Pros and Cons

### Pros:

- **Stable**: Preserves the order of equal elements.
- **Predictable Performance**: Consistently O(n log n) time complexity.
- **Efficient for Large Datasets**: Works well with large datasets, especially when they don't fit into memory (external sorting).
- **Good for Linked Lists**: Performs better than QuickSort on linked lists.

### Cons:

- **Requires Extra Space**: Requires additional O(n) memory for arrays.
