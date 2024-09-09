# Integer Reversion Exercise

## Problem Statement

Your task is to design an efficient algorithm to reverse a given integer. For example, if the input of the algorithm is `1234`, then the output should be `4321`.

### Example:

- Input: `1234`
- Output: `4321`

- Input: `-5678`
- Output: `-8765`

### Note:

- The input is an **integer** (not a string), and the algorithm must handle both positive and negative numbers.
- You should achieve the solution with **O(N)** time complexity, where `N` is the number of digits in the integer.

## Approach:

To reverse an integer:

1. **Extract the last digit** of the number by using modulo (`% 10`).
2. **Construct the reversed number** by multiplying the current reversed number by 10 and adding the extracted digit.
3. **Remove the last digit** of the original number by performing an integer division by 10 (`// 10`).
4. **Handle negative numbers** by checking the sign of the input and applying the negative sign to the result if necessary.

## Time Complexity:

- The time complexity of this approach is **O(N)**, where `N` is the number of digits in the integer. Each digit is processed once, so the runtime is proportional to the number of digits.
