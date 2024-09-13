# String Encode and Decode

## Problem Statement

Design an algorithm to encode a list of strings into a single string. The encoded string can then be decoded back into the original list of strings.

## Examples

**Example 1:**

- **Input:** `["neet","code","love","you"]`
- **Output:** `["neet","code","love","you"]`

**Example 2:**

- **Input:** `["we","say",":","yes"]`
- **Output:** `["we","say",":","yes"]`

## Solution

The solution involves two methods:

1.  **`encode`**: Converts a list of strings into a single encoded string.
2.  **`decode`**: Converts the encoded string back into the original list of strings.

### `encode`

Encodes a list of strings into a single string. Each string is preceded by its length followed by a delimiter (`#`).

#### Implementation

```python
def encode(self, strs: List[str]) -> str:
    encoded = ''
    for word in strs:
        characters = len(word)
        encoded += f'{characters}#{word}'
    return encoded
```

### `decode`

Decodes the previously encoded string back into the list of original strings. It extracts each string based on its length indicated before the delimiter.

#### Implementation

```python
def decode(self, s: str) -> List[str]:
    res, i = [], 0

    while i < len(s):
        j = i

        while s[j] != '#':
            j += 1
        length = int(s[i:j])
        res.append(s[j+1 : j+1+length])
        i = j+1+length

    return res
```

### Explanation

1.  **Encoding:**

    - Iterate through each string in the list.
    - Prepend the length of each string followed by a delimiter (`#`).
    - Concatenate these into a single encoded string.

2.  **Decoding:**

    - Read the encoded string.
    - For each encoded segment, extract the length of the original string from the segment.
    - Use the length to slice the encoded string to retrieve the original string.
    - Repeat until the entire string is processed.

### Complexity

- **Time Complexity:** O(n), where nnn is the total number of characters in the encoded string.
- **Space Complexity:** O(n), where nnn is the total number of characters in the encoded string.
