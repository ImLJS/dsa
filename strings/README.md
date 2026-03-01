# 🔤 Strings

> Strings are character arrays — most array patterns apply, with extra focus on palindromes and encoding.

---

## Patterns Overview

| Pattern | When to Use | Key Idea |
|---------|------------|---------|
| [Sliding Window](#-sliding-window-on-strings) | Substring with constraint | Expand right, shrink left |
| [Two Pointers](#-two-pointers-on-strings) | Palindromes, reversals | Compare from both ends inward |
| [HashMap / Anagram](#-hashmap--anagram--encoding) | Frequency match, encoding | Character count comparison |
| [String Parsing & Math](#-string-parsing--math) | Numbers, expressions, nested brackets | Character-by-character with stack |

---

## 🪟 Sliding Window on Strings

**When to use:** Substring with a constraint — no repeats, at most k distinct chars, anagram match, minimum covering window.

**Trigger keywords:** "longest substring without", "minimum window", "permutation in string", "find all anagrams"

```python
from collections import defaultdict

def sliding_window_string(s, t):
    need = Counter(t)
    have = {}
    formed = 0        # how many chars satisfy the required frequency
    required = len(need)
    left = 0
    result = ""

    for right, char in enumerate(s):
        have[char] = have.get(char, 0) + 1
        if char in need and have[char] == need[char]:
            formed += 1

        while formed == required:
            # Update result
            if not result or right - left + 1 < len(result):
                result = s[left:right+1]
            # Shrink window
            have[s[left]] -= 1
            if s[left] in need and have[s[left]] < need[s[left]]:
                formed -= 1
            left += 1

    return result
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Longest Substring Without Repeating Characters | #3 | 🟡 Medium | Set/dict + shrink on duplicate |
| Longest Repeating Character Replacement | #424 | 🟡 Medium | `max_freq + window_size` rule |
| Minimum Window Substring | #76 | 🔴 Hard | Two freq maps + have/need counters |
| Find All Anagrams in a String | #438 | 🟡 Medium | Fixed-size frequency comparison |
| Permutation in String | #567 | 🟡 Medium | Fixed window of `len(s1)` |
| Longest Substring with At Most K Distinct | #340 | 🟡 Medium | HashMap count, shrink when > k |

---

## ↩️ Two Pointers on Strings

**When to use:** Palindrome checks, in-place reversals, comparing characters from both ends inward.

**Trigger keywords:** "palindrome", "reverse words", "valid palindrome"

```python
# Palindrome check
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Expand around centre (longest palindromic substring)
def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]   # last valid window

result = ""
for i in range(len(s)):
    odd  = expand(s, i, i)       # odd length
    even = expand(s, i, i+1)     # even length
    result = max(result, odd, even, key=len)
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Valid Palindrome | #125 | 🟢 Easy | `isalnum()` filter + two pointers inward |
| Valid Palindrome II | #680 | 🟢 Easy | Try skipping one char from either side |
| Reverse Words in a String | #151 | 🟡 Medium | Split + reverse list + rejoin |
| Longest Palindromic Substring | #5 | 🟡 Medium | Expand around each possible centre |
| Palindromic Substrings — count all | #647 | 🟡 Medium | Expand and count each valid range |

---

## 🔣 HashMap / Anagram / Encoding

**When to use:** Character frequency comparison, encoding unique patterns, or bidirectional character mapping.

**Trigger keywords:** "anagram", "isomorphic", "word pattern", "group by"

```python
from collections import Counter

# Anagram check
Counter(s) == Counter(t)

# Group anagrams — sorted word as key
from collections import defaultdict
groups = defaultdict(list)
for word in words:
    groups[tuple(sorted(word))].append(word)

# Isomorphic — bidirectional mapping
def is_isomorphic(s, t):
    s_to_t, t_to_s = {}, {}
    for cs, ct in zip(s, t):
        if cs in s_to_t and s_to_t[cs] != ct: return False
        if ct in t_to_s and t_to_s[ct] != cs: return False
        s_to_t[cs] = ct
        t_to_s[ct] = cs
    return True
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Valid Anagram | #242 | 🟢 Easy | Counter comparison in O(n) |
| Group Anagrams | #49 | 🟡 Medium | `sorted(word)` as the hashmap key |
| Isomorphic Strings | #205 | 🟢 Easy | Dual hashmap bidirectional mapping |
| Word Pattern | #290 | 🟢 Easy | Map words to chars and chars to words |
| Encode and Decode Strings | #271 | 🟡 Medium | Length-prefix encoding trick |

---

## 🔢 String Parsing & Math

**When to use:** String represents a number, expression, or nested structure requiring careful parsing.

**Trigger keywords:** "decode", "evaluate", "parse", "convert"

```python
# Decode String — stack for nested brackets
def decode_string(s):
    stack = []
    current = ""
    k = 0

    for ch in s:
        if ch.isdigit():
            k = k * 10 + int(ch)
        elif ch == '[':
            stack.append((current, k))
            current, k = "", 0
        elif ch == ']':
            prev, num = stack.pop()
            current = prev + num * current
        else:
            current += ch
    return current
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| String to Integer (atoi) | #8 | 🟡 Medium | Handle sign, overflow, non-digit chars |
| Multiply Strings | #43 | 🟡 Medium | Grade-school multiplication on digit arrays |
| Decode String | #394 | 🟡 Medium | Stack for nested `[ ]` bracket expansion |
| Count and Say | #38 | 🟡 Medium | Run-length encoding built iteratively |

---

## 🔀 Combined Practice

> These problems require mixing 2+ patterns. Spend 15+ minutes before checking hints.

| Problem | LC # | Difficulty | Patterns Required |
|---------|------|-----------|------------------|
| Minimum Window Substring | #76 | 🔴 Hard | Sliding Window + HashMap |
| Interleaving String | #97 | 🟡 Medium | 2D DP + String Parsing |
| Longest Palindromic Subsequence | #516 | 🟡 Medium | 2D DP on reversed string (LCS) |
| String Compression | #443 | 🟡 Medium | Two Pointer in-place write-head |
| Word Break II — all sentences | #140 | 🔴 Hard | Sliding Window + DP + Backtracking |
| Regular Expression Matching | #10 | 🔴 Hard | 2D DP handling `.` and `*` transitions |

---

## 📚 Resources

| Resource | Link | Best For |
|----------|------|---------|
| NeetCode Strings Playlist | youtube.com/@NeetCode | Pattern-focused video walkthroughs |
| LeetCode Explore — Strings | leetcode.com/explore/learn/card/array-and-string | String manipulation exercises |
| Python String Docs | docs.python.org/3/library/stdtypes.html | All built-in string methods |

---

## 🐍 Python Tips

```python
# All string methods
s.split()               # split on whitespace
" ".join(lst)           # join list into string
s.strip()               # remove leading/trailing whitespace
s.lower() / s.upper()
s[::-1]                 # reverse string
s.isalnum()             # True if alphanumeric
s.isdigit()             # True if all digits

# Check all chars in set
all(c in "aeiou" for c in s)

# Counter for frequency
from collections import Counter
freq = Counter(s)
freq.most_common(3)     # [('a', 5), ('b', 3), ...]
```