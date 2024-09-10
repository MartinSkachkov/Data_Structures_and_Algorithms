# Duplicate Integer Problem Solutions

## Problem Statement

Given an integer array `nums`, return `true` if any value appears more than once in the array; otherwise, return `false`.

### Example 1:

- **Input:** `nums = [1, 2, 3, 3]`
- **Output:** `true`

### Example 2:

- **Input:** `nums = [1, 2, 3, 4]`
- **Output:** `false`

## Solution 1: Brute Force Approach

This solution compares every element with every other element in the list to check for duplicates.

```python
def hasDuplicate(nums: list[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
```

### Explanation

- We use two nested loops. The outer loop picks each element, and the inner loop checks for duplicates by comparing it with every other element in the list.
- If a duplicate is found, it returns `True`; otherwise, after checking all pairs, it returns `False`.

### Time Complexity

- **Worst-case time complexity:** O(n²), where `n` is the length of the input list `nums`. This is because for each element, we iterate through the remaining elements to check for duplicates.

### Space Complexity

- **Space complexity:** O(1), as no extra space is used apart from a few variables.

## Solution 2: Sorting Approach

This solution sorts the array and checks adjacent elements for duplicates.

```python
def hasDuplicate2(nums: list[int]) -> bool:
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False`
```

### Explanation

- First, we sort the array, which brings any duplicates next to each other.
- We then iterate through the array and compare adjacent elements. If any two consecutive elements are equal, a duplicate is found, and `True` is returned.

### Time Complexity

- **Worst-case time complexity:** O(n log n), where `n` is the length of the input list `nums`. This comes from the time complexity of sorting the list.

### Space Complexity

- **Space complexity:** O(1) if the sorting is done in place (as no extra space is used other than a few variables), or O(n) if a new sorted list is created.

## Solution 3: Hash Set Approach

This solution uses a hash set to keep track of elements that have already been encountered.

```python
def hasDuplicate3(nums: list[int]) -> bool:
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False
```

### Explanation

- We iterate through the list and for each element, check if it's already in the hash set.
- If the element is found in the hash set, it means we've encountered a duplicate, and `True` is returned.
- If not, the element is added to the hash set for future reference.

### Time Complexity

- **Worst-case time complexity:** O(n), where `n` is the length of the input list `nums`. This is because each lookup and insertion operation in a hash set has an average time complexity of O(1).

### Space Complexity

- **Space complexity:** O(n), as we use extra space to store elements in a hash set.

## Summary of Time and Space Complexities

| Solution        | Time Complexity | Space Complexity |
| --------------- | --------------- | ---------------- |
| **Brute Force** | O(n²)           | O(1)             |
| **Sorting**     | O(n log n)      | O(1) or O(n)     |
| **Hash Set**    | O(n)            | O(n)             |

Each solution has different trade-offs. The brute force approach is simple but inefficient, especially for large arrays. The sorting approach is better but still has a higher time complexity due to sorting. The hash set approach provides the best performance for this problem with O(n) time complexity.
