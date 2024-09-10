# Anagram Problem Exercise

## Problem Statement

An **anagram** is a word or phrase formed by rearranging the letters of another word or phrase, typically using all the original letters exactly once.

### Task:

Your task is to construct an algorithm to check whether two given words (or phrases) are anagrams of each other.

### Example:

- Input: `"restful"` and `"fluster"`

  - Output: **True** (They are anagrams)

- Input: `"apple"` and `"pale"`
  - Output: **False** (They are not anagrams)

## Approach:

To check if two words or phrases are anagrams:

1. **Sort and Compare**: Sort the characters of both words. If the sorted characters match, the words are anagrams.
2. Alternatively, you can **count the frequency of each letter** in both words using a hash map or a dictionary. If the frequency of each character is the same for both words, they are anagrams.

## Time Complexity:

- The time complexity is **O(N log N)** when using the sorting approach, where `N` is the length of the strings. Sorting is the most time-consuming step.
- If using the frequency-counting approach, the time complexity is **O(N)**, where `N` is the length of the strings.
