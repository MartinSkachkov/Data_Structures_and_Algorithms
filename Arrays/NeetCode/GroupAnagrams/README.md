# Anagram Groups

This repository provides a solution for grouping anagrams from a list of strings. An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

## Problem Statement

Given an array of strings `strs`, group all anagrams together into sublists. You may return the output in any order.

### Examples

**Example 1:**

**Input:** `strs = ["act","pots","tops","cat","stop","hat"]`

**Output:** `[["hat"],["act", "cat"],["stop", "pots", "tops"]]`

**Example 2:**

**Input:** `strs = ["x"]`

**Output:** `[["x"]]`

**Example 3:**

**Input:** `strs = [""]`

**Output:** `[[""]]`

## Solution

The provided solution uses a dictionary to group anagrams efficiently. Here's the code:

```python
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)

    for s in strs:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord("a")] += 1

        res[tuple(count)].append(s)

    return list(res.values())
```

### Explanation

1.  **Initialization**: A `defaultdict` of lists is used to store the grouped anagrams.
2.  **Counting Characters**: For each string, we count the occurrences of each character and store this count as a tuple.
3.  **Grouping**: We use the tuple of character counts as the key in our dictionary, appending the original string to the list corresponding to this key.
4.  **Returning Results**: Finally, we return the grouped anagrams as a list of lists.

## Time Complexity

- **O(N \* K)**: Where `N` is the number of strings in the input list `strs`, and `K` is the maximum length of a string. This is because, for each string, we count its characters, which takes `O(K)` time, and we do this for `N` strings.

## Space Complexity

- **O(N \* K)**: The space complexity is primarily due to storing the results in the dictionary and the final output list. In the worst case, all strings are anagrams of each other and are stored together, taking `O(N * K)` space.
