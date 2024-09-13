# Product of Array Except Self

## Problem Statement

Given an integer array `nums`, the task is to return an array `output` where `output[i]` is the product of all the elements of `nums` except `nums[i]`.

### Follow-up

Can you solve it in O(n) time without using the division operation?

### Examples

**Example 1:**

- **Input:** `nums = [1,2,4,6]`
- **Output:** `[48,24,12,8]`

**Example 2:**

- **Input:** `nums = [-1,0,1,2,3]`
- **Output:** `[0,-6,0,0,0]`

## Solution

The solution avoids the use of division and achieves O(n) time complexity by using two passes through the array: one for the prefix products and one for the suffix products.

Here's the implementation of the solution:

```python
def productExceptSelf(nums: List[int]) -> List[int]:
    output = [1] * len(nums)  # Initialize the output array with 1s
    pref = 1

    # Calculate prefix products
    for i in range(len(nums)):
        output[i] = pref
        pref *= nums[i]

    suff = 1
    # Calculate suffix products and update the output array
    for i in range(len(nums) - 1, -1, -1):
        output[i] *= suff
        suff *= nums[i]

    return output
```

### Explanation

1.  **Initialization:**

    - Create an `output` list initialized with `1`s. This will hold the final product values.

2.  **Prefix Products Calculation:**

    - Iterate through the list and compute the prefix product for each element. Store these products in the `output` list.

3.  **Suffix Products Calculation:**

    - Iterate through the list in reverse to compute the suffix product for each element and update the `output` list by multiplying it with the current suffix product.

### Complexity

- **Time Complexity:** O(n), where nnn is the length of the `nums` array.
- **Space Complexity:** O(1) (excluding the output array).
