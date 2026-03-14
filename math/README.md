# 🔢 Math & Number Theory

> Number theory, combinatorics, geometry basics, and pure math tricks. These problems don't fit neatly into data structure categories — the key insight is always mathematical.

---

## Patterns Overview

| Pattern | When to Use |
|---------|------------|
| [Modular Arithmetic](#-modular-arithmetic) | Large numbers, avoid overflow |
| [GCD / LCM](#-gcd--lcm) | Divisibility, fraction reduction |
| [Prime Numbers](#-prime-numbers--sieve) | Factor problems, primality checks |
| [Fast Exponentiation](#-fast-exponentiation) | x^n in O(log n) |
| [Combinatorics](#-combinatorics) | Count arrangements, Pascal's triangle |
| [Geometry & Coordinates](#-geometry--coordinates) | Points, slopes, areas |
| [Number Properties](#-number-properties) | Digit tricks, overflow, special sequences |

---

## 🔁 Modular Arithmetic

**When to use:** Any problem asking for result "mod 10^9+7". Prevents integer overflow in large computations.

```python
MOD = 10**9 + 7

# Key properties
(a + b) % MOD == ((a % MOD) + (b % MOD)) % MOD
(a * b) % MOD == ((a % MOD) * (b % MOD)) % MOD
(a - b) % MOD == ((a % MOD) - (b % MOD) + MOD) % MOD   # add MOD to stay positive

# Division mod p — use modular inverse (only when MOD is prime)
# a / b mod p = a * pow(b, p-2, p) mod p   (Fermat's little theorem)
def mod_divide(a, b, p=MOD):
    return (a * pow(b, p - 2, p)) % p

# Python built-in pow handles modular exponentiation efficiently
pow(base, exp, mod)   # = (base^exp) % mod in O(log exp)
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Fibonacci Number | #509 | 🟢 Easy | Matrix exponentiation for O(log n) |
| Unique Paths | #62 | 🟡 Medium | C(m+n-2, m-1) — combinatorics |
| Count Vowels Permutation | #1220 | 🔴 Hard | DP + modular arithmetic |

---

## ➗ GCD / LCM

**When to use:** Fraction simplification, finding common periods, divisibility problems.

```python
import math

# GCD — Euclidean algorithm
math.gcd(a, b)          # built-in, O(log min(a,b))

# Manual GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# LCM
def lcm(a, b):
    return a * b // math.gcd(a, b)

# GCD of a list
from functools import reduce
reduce(math.gcd, nums)

# Extended Euclidean — find x, y such that ax + by = gcd(a,b)
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Greatest Common Divisor of Strings | #1071 | 🟢 Easy | GCD of lengths gives answer length |
| Find GCD of Array | #1979 | 🟢 Easy | GCD of min and max elements |
| X of a Kind in a Deck of Cards | #914 | 🟢 Easy | GCD of all group sizes must be >= 2 |
| Nth Magical Number | #878 | 🔴 Hard | Binary Search + LCM inclusion-exclusion |

---

## 🔢 Prime Numbers & Sieve

**When to use:** Count primes, factor numbers, check primality.

```python
# Sieve of Eratosthenes — all primes up to n in O(n log log n)
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [i for i in range(n+1) if is_prime[i]]


# Primality check — O(sqrt(n))
def is_prime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0: return False
        i += 6
    return True


# Prime factorisation
def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Count Primes | #204 | 🟡 Medium | Sieve of Eratosthenes |
| Ugly Number | #263 | 🟢 Easy | Only prime factors 2, 3, 5 |
| Ugly Number II | #264 | 🟡 Medium | Min-heap: multiply each by 2, 3, 5 |
| Largest Component Size by Common Factor | #952 | 🔴 Hard | Sieve-style + Union-Find on factors |

---

## ⚡ Fast Exponentiation

**When to use:** Compute x^n efficiently. Also applies to matrix exponentiation for linear recurrences.

```python
# Iterative fast power — O(log n)
def fast_pow(base, exp, mod=None):
    result = 1
    base = base % mod if mod else base
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod if mod else result * base
        base = (base * base) % mod if mod else base * exp
        exp //= 2
    return result

# Python built-in (always prefer this)
pow(base, exp)          # fast exponentiation
pow(base, exp, mod)     # modular fast exponentiation


# Matrix exponentiation — Fibonacci in O(log n)
def mat_mul(A, B, mod):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
    return C

def mat_pow(M, p, mod):
    n = len(M)
    result = [[1 if i==j else 0 for j in range(n)] for i in range(n)]  # identity
    while p:
        if p & 1: result = mat_mul(result, M, mod)
        M = mat_mul(M, M, mod)
        p >>= 1
    return result
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Pow(x, n) | #50 | 🟡 Medium | Fast exponentiation, handle negative n |
| Super Pow | #372 | 🟡 Medium | Modular exponentiation digit by digit |

---

## 🎲 Combinatorics

**When to use:** Count arrangements, selections, or paths. Pascal's triangle precomputes C(n, k) for all n, k.

```python
# C(n, k) — choose k from n
from math import comb
comb(n, k)      # built-in Python 3.8+

# Manual — O(k) time
def choose(n, k):
    if k > n: return 0
    k = min(k, n - k)   # C(n,k) == C(n,n-k)
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result


# Pascal's Triangle — precompute all C(i,j) up to n
def pascal(n):
    C = [[0] * (n+1) for _ in range(n+1)]
    for i in range(n+1):
        C[i][0] = 1
        for j in range(1, i+1):
            C[i][j] = C[i-1][j-1] + C[i-1][j]
    return C


# Factorial + modular inverse for large C(n,k) mod p
MOD = 10**9 + 7

def precompute_factorials(n):
    fact = [1] * (n + 1)
    for i in range(1, n+1):
        fact[i] = fact[i-1] * i % MOD
    inv_fact = [1] * (n + 1)
    inv_fact[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n-1, -1, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
    return fact, inv_fact

def comb_mod(n, k, fact, inv_fact):
    if k < 0 or k > n: return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n-k] % MOD
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Pascal's Triangle | #118 | 🟢 Easy | `C[i][j] = C[i-1][j-1] + C[i-1][j]` |
| Pascal's Triangle II | #119 | 🟢 Easy | Single row — update in reverse |
| Unique Paths | #62 | 🟡 Medium | `C(m+n-2, m-1)` paths in a grid |
| Kth Row of Pascal's Triangle | #119 | 🟢 Easy | Roll the row in-place |

---

## 📐 Geometry & Coordinates

```python
# Slope between two points
def slope(p1, p2):
    if p2[0] == p1[0]: return float('inf')
    return (p2[1] - p1[1]) / (p2[0] - p1[0])

# Area of triangle given 3 points (cross product / shoelace)
def triangle_area(p1, p2, p3):
    return abs((p2[0]-p1[0])*(p3[1]-p1[1]) - (p3[0]-p1[0])*(p2[1]-p1[1])) / 2

# Distance squared (avoid float)
def dist_sq(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

# Check collinear — cross product == 0
def collinear(p1, p2, p3):
    return (p2[0]-p1[0])*(p3[1]-p1[1]) == (p3[0]-p1[0])*(p2[1]-p1[1])
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Max Points on a Line | #149 | 🔴 Hard | Fix one point, count max slope matches |
| Valid Boomerang | #1037 | 🟢 Easy | 3 non-collinear points — cross product != 0 |
| Minimum Area Rectangle | #939 | 🟡 Medium | Fix diagonal pair, check other two corners exist |

---

## 🔢 Number Properties

```python
# Digit extraction
def digits(n):
    result = []
    while n:
        result.append(n % 10)
        n //= 10
    return result[::-1]

# Digit sum
def digit_sum(n):
    return sum(int(d) for d in str(n))

# Check palindrome number
def is_palindrome(n):
    if n < 0: return False
    s = str(n)
    return s == s[::-1]

# Integer square root (no float)
import math
math.isqrt(n)           # floor(sqrt(n)) — exact integer
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Palindrome Number | #9 | 🟢 Easy | Reverse half the digits, compare |
| Reverse Integer | #7 | 🟡 Medium | Handle overflow — check before multiplying |
| Happy Number | #202 | 🟢 Easy | Digit sum cycle — use Floyd's or set |
| Integer to Roman | #12 | 🟡 Medium | Greedy from largest denomination down |
| Excel Sheet Column Number | #171 | 🟢 Easy | Base-26 number system |
| Sqrt(x) | #69 | 🟢 Easy | Binary search on answer |
| Fraction to Recurring Decimal | #166 | 🟡 Medium | Long division + detect remainder cycle |

---

## 📚 Resources

| Resource | Link | Best For |
|----------|------|---------|
| CP-Algorithms Math | cp-algorithms.com/algebra | GCD, sieve, fast pow, combinatorics |
| NeetCode Math & Geometry | youtube.com/@NeetCode | Problem walkthroughs |

---

## 🐍 Python Tips

```python
import math

math.gcd(a, b)          # GCD
math.lcm(a, b)          # LCM (Python 3.9+)
math.isqrt(n)           # Integer square root
math.comb(n, k)         # Combinations C(n,k) (Python 3.8+)
math.factorial(n)       # n!
math.log(n, base)       # log base

# Infinity
float('inf')
float('-inf')

# Modular arithmetic
pow(base, exp, mod)     # fast modular exponentiation

# Integer division and modulo
a // b                  # floor division
a % b                   # always non-negative in Python
divmod(a, b)            # returns (quotient, remainder)
```