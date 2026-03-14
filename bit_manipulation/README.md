# 🔢 Bit Manipulation

> Operate directly on binary representations. Constant space, extremely fast. Most patterns reduce to 5-6 core tricks — learn those and you can solve almost any bit problem.

---

## Core Operations

```python
# AND  — keeps bits set in BOTH
a & b

# OR   — keeps bits set in EITHER
a | b

# XOR  — keeps bits set in ONE but not both (toggle, find difference)
a ^ b

# NOT  — flip all bits
~a

# Left shift  — multiply by 2^n
a << n

# Right shift — divide by 2^n
a >> n
```

---

## Essential Tricks

```python
# Check if bit i is set
(n >> i) & 1

# Set bit i
n | (1 << i)

# Clear bit i
n & ~(1 << i)

# Toggle bit i
n ^ (1 << i)

# Check if n is a power of 2
n > 0 and (n & (n - 1)) == 0

# Remove the lowest set bit (Brian Kernighan)
n & (n - 1)

# Get the lowest set bit
n & (-n)

# Count set bits
bin(n).count('1')
# Or: use bit_count() in Python 3.10+
n.bit_count()

# XOR all numbers from 1 to n
# n%4==0: n, n%4==1: 1, n%4==2: n+1, n%4==3: 0

# Swap without temp variable
a ^= b
b ^= a
a ^= b
```

---

## Patterns

### XOR Tricks

**When to use:** Find the element that appears an odd number of times. XOR of a number with itself = 0. XOR with 0 = number itself.

```python
# Find single number — all others appear twice
def single_number(nums):
    result = 0
    for n in nums:
        result ^= n     # duplicates cancel out
    return result


# Find two single numbers — all others appear twice
def single_number_iii(nums):
    xor = 0
    for n in nums: xor ^= n     # xor = a ^ b (the two singles)

    # Find any bit that differs between a and b
    diff_bit = xor & (-xor)     # lowest set bit

    a = 0
    for n in nums:
        if n & diff_bit:
            a ^= n      # XOR numbers with that bit set
    return [a, xor ^ a]


# Missing number — 0 to n, one missing
def missing_number(nums):
    result = len(nums)
    for i, n in enumerate(nums):
        result ^= i ^ n
    return result
```

### Bit Counting

```python
# Count set bits (Hamming weight)
def hamming_weight(n):
    count = 0
    while n:
        n &= n - 1      # remove lowest set bit
        count += 1
    return count


# Count bits for 0..n — DP
def count_bits(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)   # dp[i/2] + last bit
    return dp


# Hamming distance between x and y
def hamming_distance(x, y):
    return bin(x ^ y).count('1')
```

### Power of 2 / Number Theory via Bits

```python
# Is power of 2?
def is_power_of_two(n):
    return n > 0 and (n & (n-1)) == 0

# Is power of 4?  (power of 2 AND set bit in odd position)
def is_power_of_four(n):
    return n > 0 and (n & (n-1)) == 0 and (n & 0xAAAAAAAA) == 0

# Reverse bits
def reverse_bits(n):
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
```

### Bitmask DP / Subsets

```python
# Enumerate all subsets of a set using bitmasks
n = 4
for mask in range(1 << n):       # 0 to 2^n - 1
    subset = [i for i in range(n) if mask & (1 << i)]

# Enumerate all subsets of a bitmask (sub-mask enumeration)
mask = 0b1101
sub = mask
while sub:
    # process sub
    sub = (sub - 1) & mask       # next smaller subset


# Bitmask DP — Travelling Salesman / assignment problems
# dp[mask][i] = min cost to visit all cities in mask, ending at city i
n = 4
dp = [[float('inf')] * n for _ in range(1 << n)]
dp[1][0] = 0   # start at city 0

for mask in range(1 << n):
    for u in range(n):
        if not (mask >> u & 1): continue
        for v in range(n):
            if mask >> v & 1: continue
            new_mask = mask | (1 << v)
            dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + dist[u][v])
```

---

## Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Single Number | #136 | 🟢 Easy | XOR all — duplicates cancel |
| Number of 1 Bits | #191 | 🟢 Easy | `n & (n-1)` removes lowest set bit |
| Counting Bits | #338 | 🟢 Easy | `dp[i] = dp[i>>1] + (i&1)` |
| Missing Number | #268 | 🟢 Easy | XOR indices and values |
| Reverse Bits | #190 | 🟢 Easy | Shift and OR bit by bit |
| Power of Two | #231 | 🟢 Easy | `n > 0 and (n & (n-1)) == 0` |
| Hamming Distance | #461 | 🟢 Easy | Count bits in `x ^ y` |
| Single Number II | #137 | 🟡 Medium | Count bits mod 3 |
| Single Number III | #260 | 🟡 Medium | XOR + split by differing bit |
| Sum of Two Integers | #371 | 🟡 Medium | `a ^ b` = sum without carry, `(a&b)<<1` = carry |
| Bitwise AND of Numbers Range | #201 | 🟡 Medium | Common prefix of all numbers in range |
| Maximum XOR of Two Numbers | #421 | 🟡 Medium | Trie on binary representation |
| Subsets (bitmask approach) | #78 | 🟡 Medium | Each subset = a bitmask from 0 to 2^n−1 |

---

## Combined Practice

| Problem | LC # | Difficulty | Patterns Required |
|---------|------|-----------|------------------|
| Maximum XOR of Two Numbers | #421 | 🟡 Medium | Bit Manipulation + Trie |
| Partition to K Equal Sum Subsets | #698 | 🟡 Medium | Bitmask DP + Backtracking |
| Shortest Path Visiting All Nodes | #847 | 🔴 Hard | Bitmask DP + BFS |
| Smallest Sufficient Team | #1125 | 🔴 Hard | Bitmask DP |

---

## 📚 Resources

| Resource | Link | Best For |
|----------|------|---------|
| NeetCode Bit Manipulation | youtube.com/@NeetCode | Core tricks with clean Python |
| CP-Algorithms Bit Tricks | cp-algorithms.com/algebra/bit-manipulation.html | Comprehensive reference |

---

## 🐍 Python Tips

```python
# Python integers have arbitrary precision — no 32-bit overflow
# But some problems assume 32-bit signed integer range

# Convert to 32-bit unsigned
n & 0xFFFFFFFF

# Bin / hex representation
bin(255)      # '0b11111111'
hex(255)      # '0xff'
int('1101', 2)   # binary string to int = 13

# Bit length
(10).bit_length()    # 4  (1010 in binary)

# Python 3.10+ — count set bits directly
n.bit_count()
```