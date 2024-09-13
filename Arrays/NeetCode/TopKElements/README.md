# Top K Frequent Elements

## Description

Given an integer array `nums` and an integer `k`, the goal is to return the `k` most frequent elements within the array. The solution ensures that the result is always unique, and you can return the output in any order.

## Example

### Example 1

**Input:**
`nums = [1, 2, 2, 3, 3, 3]
k = 2`

**Output:**
`[2, 3]`

### Example 2

**Input:**
`nums = [7, 7]
k = 1`

**Output:**
`[7]`

## Implementation

```python
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    dp = [[] for _ in range(len(nums) + 1)]
    count = {}

    for el in nums:
        if el in count:
            count[el] += 1
        else:
            count[el] = 1

    for key, c in count.items():
        dp[c].append(key)

    res = []
    for i in range(len(nums), -1, -1):
        if k == 0:
            break
        elif dp[i] == []:
            continue
        else:
            res.extend(dp[i])
            k -= len(dp[i])

    return res
```

## Explanation

1.  **Count Frequencies**: A dictionary `count` is used to count the frequency of each element in the `nums` array.
2.  **Group by Frequency**: `dp` is a list where each index represents a frequency and contains a list of elements that have that frequency.
3.  **Collect Results**: Starting from the highest frequency, collect elements until the `k` most frequent elements are found.

## Notes

- The function runs in O(N) time complexity where N is the number of elements in `nums` due to counting and grouping operations.
- Space complexity is O(N) as it stores the counts and grouped elements.
