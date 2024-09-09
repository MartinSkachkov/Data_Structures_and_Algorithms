# Palindrome Exercise

## Problem Statement

A **palindrome** is a string that reads the same forward and backward. For example:

- "radar"
- "madam"
- "level"

Our task is to design an algorithm to check whether a given string is a palindrome or not. The goal is to implement the solution with **O(N)** linear time complexity, where `N` is the length of the string.

## Example:

### Input:

- `"radar"`
- `"hello"`

### Output:

- `"radar"` is a palindrome.
- `"hello"` is not a palindrome.

## Approach:

1. **Two-pointer technique**:

   - Use two pointers: one starting at the beginning (`left`) and one at the end (`right`) of the string.
   - Compare the characters at these pointers.
   - If the characters are the same, move the pointers towards the center and repeat.
   - If the characters do not match at any point, the string is not a palindrome.
   - If all characters match, the string is a palindrome.

2. **Time Complexity**:

   - The algorithm has **O(N)** time complexity, where `N` is the length of the string. We only need to traverse the string once to check for a palindrome.

3. **Space Complexity**:
   - The algorithm has **O(1)** space complexity since it uses a constant amount of extra space (just for the two pointers).
