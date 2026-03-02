# 🟢 Arrays — Basics

> Warm-up problems that don't require a named pattern. Solve these by reading carefully and simulating directly. Code goes in `problems/misc/`.

---

## What belongs here?

Problems solved by:
- Direct simulation — do exactly what the problem says
- Simple arithmetic or index math
- Basic iteration with no clever trick needed
- Built-in Python operations (sum, sort, reverse, count)

If you find yourself reaching for a hashmap, two pointers, or prefix sum — the problem belongs in one of the pattern folders instead.

---

## Problem List

| Problem | LC # | Difficulty | What It Practices | File |
|---------|------|-----------|------------------|------|
| Concatenation of Array | #1929 | 🟢 Easy | `nums + nums` — index math | `concatenation_of_array.py` |
| Running Sum of 1D Array | #1480 | 🟢 Easy | In-place prefix sum | `running_sum.py` |
| Shuffle the Array | #1470 | 🟢 Easy | Interleaving two halves | `shuffle_the_array.py` |
| Kids With the Greatest Candies | #1431 | 🟢 Easy | Comparison with running max | `kids_with_candies.py` |
| Richest Customer Wealth | #1672 | 🟢 Easy | Row sum, track maximum | `richest_customer_wealth.py` |
| Number of Good Pairs | #1512 | 🟢 Easy | Count matching index pairs | `number_of_good_pairs.py` |
| How Many Numbers Smaller Than Current | #1365 | 🟢 Easy | Sort + index lookup | `smaller_than_current.py` |
| Find the Difference of Two Arrays | #2215 | 🟢 Easy | Set difference both directions | `difference_of_arrays.py` |
| Move Zeroes | #283 | 🟢 Easy | In-place write-head | `move_zeroes.py` |
| Remove Element | #27 | 🟢 Easy | Write-head, skip target value | `remove_element.py` |
| Replace Elements with Greatest on Right | #1299 | 🟢 Easy | Scan right to left, track max | `replace_with_greatest.py` |
| Sort Array By Parity | #905 | 🟢 Easy | Partition evens to front | `sort_array_by_parity.py` |
| Matrix Diagonal Sum | #1572 | 🟢 Easy | Index math for diagonals | `diagonal_sum.py` |
| Flipping an Image | #832 | 🟢 Easy | Reverse row + flip bits | `flipping_an_image.py` |
| Transpose Matrix | #867 | 🟢 Easy | `zip(*matrix)` | `transpose_matrix.py` |
| Reshape the Matrix | #566 | 🟡 Medium | Flatten + reshape with index math | `reshape_matrix.py` |
| Spiral Matrix | #54 | 🟡 Medium | Layer-by-layer boundary simulation | `spiral_matrix.py` |
| Rotate Image | #48 | 🟡 Medium | Transpose then reverse each row | `rotate_image.py` |

---

## Solution Template

```python
"""
Problem: Concatenation of Array (#1929)
Difficulty: Easy
Link: https://leetcode.com/problems/concatenation-of-array/

Approach:
- Return nums concatenated with itself
- In Python, nums + nums does this directly

Time:  O(n)
Space: O(n)
"""

def getConcatenation(nums):
    return nums + nums
```

---

## Python One-liners for Basics Problems

```python
# Concatenate array with itself
nums + nums

# Sum of all elements
sum(nums)

# Max element
max(nums)

# Running sum in-place
for i in range(1, len(nums)):
    nums[i] += nums[i - 1]

# Reverse a list
nums[::-1]
nums.reverse()      # in-place

# Digit extraction
digits = []
while n:
    digits.append(n % 10)
    n //= 10
digits.reverse()    # now MSB first

# Flatten 2D list
[x for row in matrix for x in row]

# Transpose matrix
list(zip(*matrix))

# Check all elements satisfy a condition
all(x > 0 for x in nums)
any(x < 0 for x in nums)

# Count occurrences of a value
nums.count(3)

# Remove duplicates preserving order
list(dict.fromkeys(nums))
```