# Two Integer Sum Problem

## Problem Description

Given an array of integers `nums` and an integer `target`, return the indices `i` and `j` such that:

- `nums[i] + nums[j] == target`
- `i != j` (i.e., the indices must be different).

You may assume that every input has **exactly one pair of indices** `i` and `j` that satisfy the condition. The function should return the indices with the **smaller index first**.

### Example 1:

Input: nums = [3, 4, 5, 6], target = 7

Output: [0, 1]

Explanation: `nums[0] + nums[1] == 7`, so we return `[0, 1]`.

### Example 2:

Input: nums = [4, 5, 6], target = 10

Output: [0, 2]

### Example 3:

Input: nums = [5, 5], target = 10

Output: [0, 1]

## Approach

This problem can be efficiently solved using a **hashmap (dictionary)** to store the numbers we've seen so far and their respective indices.

### Algorithm:

1. **Initialize an empty hashmap**: This hashmap will store each number as the key and its index as the value.
2. **Iterate over the array**: For each element `el` in `nums`, compute its complement, which is `target - el`.
3. **Check if the complement is in the hashmap**: If it is, return the index of the complement and the current index because we've found the two numbers that add up to the target.
4. **If the complement is not found**: Store the current number and its index in the hashmap for future reference.
5. **Return the indices**: Since the problem guarantees that exactly one solution exists, the function will always return a result.

### Time Complexity:

- **O(n)** where `n` is the number of elements in `nums`. We only traverse the array once and perform O(1) hashmap operations (insertions and lookups).

### Space Complexity:

- **O(n)** due to the extra space needed to store elements in the hashmap.

## Solution

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # Dictionary to store the number and its index

        idx = 0  # Initialize the index

        for el in nums:
            complement = target - el  # Calculate the complement

            # If complement is in the hashmap, return the indices
            if complement in hashmap:
                return [hashmap[complement], idx]

            # Otherwise, add the current element to the hashmap
            hashmap[el] = idx
            idx += 1

        # Since the problem guarantees a solution, no need for an additional return here
```

### Example Walkthrough:

For `nums = [3, 4, 5, 6]` and `target = 7`:

- At index `0`, the number is `3`, and the complement is `4`. `4` is not in the hashmap.
- At index `1`, the number is `4`, and the complement is `3`. `3` is in the hashmap at index `0`, so we return `[0, 1]`.

For `nums = [4, 5, 6]` and `target = 10`:

- At index `0`, the number is `4`, and the complement is `6`. `6` is not in the hashmap.
- At index `1`, the number is `5`, and the complement is `5`. `5` is not in the hashmap.
- At index `2`, the number is `6`, and the complement is `4`. `4` is in the hashmap at index `0`, so we return `[0, 2]`.

## Edge Cases:

1.  **Duplicate numbers**: The algorithm handles cases like `[5, 5]` with target `10`, where both numbers are the same, correctly returning `[0, 1]`.
2.  **Negative numbers**: The approach works for arrays with negative numbers as well.
