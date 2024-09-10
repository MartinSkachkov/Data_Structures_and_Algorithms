# Is Anagram Problem Solutions

## Problem Statement

Given two strings `s` and `t`, return `true` if the two strings are anagrams of each other, otherwise return `false`.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

### Example 1:

- **Input:** `s = "racecar"`, `t = "carrace"`
- **Output:** `true`

### Example 2:

- **Input:** `s = "jar"`, `t = "jam"`
- **Output:** `false`

### Constraints:

- `s` and `t` consist of lowercase English letters.

## Solution 1: Counting Characters

This solution uses two dictionaries to count the frequency of each character in the strings and then compares these counts.

```python
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in s:
        if countS[c] != countT.get(c, 0):
            return False
    return True
```

### Explanation

- We first check if the lengths of the strings are the same. If not, they cannot be anagrams.
- We then create two dictionaries to count the occurrences of each character in `s` and `t`.
- Finally, we compare the counts for each character in `s` with those in `t`.

### Time Complexity

- **Worst-case time complexity:** O(n), where `n` is the length of the strings `s` and `t`. This is because we make a single pass through the strings to build the dictionaries and another pass to compare them.

### Space Complexity

- **Space complexity:** O(1), as the space used for the dictionaries is constant with respect to the input size (bounded by the number of distinct characters, which is constant for lowercase English letters).

## Solution 2: Sorting

This solution sorts both strings and compares them to check for anagrams.

```python
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_sorted = sorted(s)
    t_sorted = sorted(t)

    return s_sorted == t_sorted
```

### Explanation

- We first check if the lengths of the strings are the same. If not, they cannot be anagrams.
- We then sort both strings and compare the sorted versions.

### Time Complexity

- **Worst-case time complexity:** O(n log n), where `n` is the length of the strings `s` and `t`. This is due to the time complexity of sorting the strings.

### Space Complexity

- **Space complexity:** O(n), where `n` is the length of the strings. This accounts for the space used by the sorted versions of the strings.

## Summary of Time and Space Complexities

| Solution                | Time Complexity | Space Complexity |
| ----------------------- | --------------- | ---------------- |
| **Counting Characters** | O(n)            | O(1)             |
| **Sorting**             | O(n log n)      | O(n)             |
