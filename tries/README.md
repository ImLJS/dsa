# 🌲 Tries (Prefix Trees)

> A tree where each node represents a character. Every path from root to a marked node spells a word. O(m) insert and search where m = word length — faster than HashMap for prefix queries.

---

## Patterns Overview

| Pattern | When to Use |
|---------|------------|
| [Basic Trie](#-basic-trie) | Insert, search, startsWith — the foundation |
| [Word Search in Grid](#-word-search-in-grid) | DFS on grid + Trie to prune dead branches |
| [Prefix Problems](#-prefix-problems) | Autocomplete, longest common prefix, replace words |

---

## Core Data Structure

```python
class TrieNode:
    def __init__(self):
        self.children = {}      # char -> TrieNode
        self.is_end   = False   # True if a word ends here


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end       # must end at a word boundary

    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True              # any node reached = valid prefix
```

---

## 🔤 Basic Trie

**When to use:** Dictionary of words needing prefix lookups, word existence, or autocomplete.

**Trigger keywords:** "dictionary", "prefix", "starts with", "autocomplete", "word exists"

```python
# Wildcard search — '.' matches any character
def search_with_wildcard(self, word):
    def dfs(node, i):
        if i == len(word):
            return node.is_end
        ch = word[i]
        if ch == '.':
            return any(dfs(child, i + 1) for child in node.children.values())
        if ch not in node.children:
            return False
        return dfs(node.children[ch], i + 1)
    return dfs(self.root, 0)
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Implement Trie (Prefix Tree) | #208 | 🟡 Medium | Textbook — build the data structure |
| Design Add and Search Words | #211 | 🟡 Medium | `.` wildcard — try all children with DFS |
| Replace Words | #648 | 🟡 Medium | Find shortest root prefix in trie, replace |
| Longest Word in Dictionary | #720 | 🟡 Medium | Only extend nodes that are valid word ends |
| Map Sum Pairs | #677 | 🟡 Medium | Store sum at each node, update on insert |

---

## 🔍 Word Search in Grid

**When to use:** Find all words from a dictionary that exist in a 2D grid. Trie prunes branches early — far faster than checking each word separately with DFS.

**Trigger keywords:** "find all words in board", "word search", "boggle"

```python
def find_words(board, words):
    root = TrieNode()
    for word in words:
        node = root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = word         # store full word at end node

    rows, cols = len(board), len(board[0])
    result = []

    def dfs(node, r, c):
        ch = board[r][c]
        if ch not in node.children:
            return
        next_node = node.children[ch]
        if hasattr(next_node, 'word') and next_node.word:
            result.append(next_node.word)
            next_node.word = None    # avoid duplicates

        board[r][c] = '#'            # mark visited
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                dfs(next_node, nr, nc)
        board[r][c] = ch             # restore

    for r in range(rows):
        for c in range(cols):
            dfs(root, r, c)

    return result
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Word Search | #79 | 🟡 Medium | DFS + backtracking on grid (no trie needed) |
| Word Search II | #212 | 🔴 Hard | DFS + Trie — prune paths not in dictionary |

---

## 🔠 Prefix Problems

**When to use:** Autocomplete, common prefix finding, grouping words by shared roots.

```python
# Autocomplete — return all words with given prefix
def autocomplete(self, prefix):
    node = self.root
    for ch in prefix:
        if ch not in node.children:
            return []
        node = node.children[ch]

    result = []
    def dfs(node, path):
        if node.is_end:
            result.append(prefix + path)
        for ch, child in node.children.items():
            dfs(child, path + ch)

    dfs(node, "")
    return result
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Longest Common Prefix | #14 | 🟢 Easy | Trie or vertical scan |
| Search Suggestions System | #1268 | 🟡 Medium | Trie + DFS for top 3 suggestions per prefix |
| Replace Words | #648 | 🟡 Medium | Find shortest prefix root, replace word |

---

## Combined Practice

| Problem | LC # | Difficulty | Patterns Required |
|---------|------|-----------|------------------|
| Word Search II | #212 | 🔴 Hard | Trie + DFS Backtracking |
| Palindrome Pairs | #336 | 🔴 Hard | Trie + palindrome check |
| Concatenated Words | #472 | 🔴 Hard | Trie + DP |
| Design Search Autocomplete System | #642 | 🔴 Hard | Trie + frequency ranking |

---

## 📚 Resources

| Resource | Link | Best For |
|----------|------|---------|
| NeetCode Trie Playlist | youtube.com/@NeetCode | Trie build + Word Search II walkthrough |
| VisuAlgo Trie | visualgo.net/en/trie | Animated insert and search |

---

## 🐍 Python Tips

```python
# Compact trie using defaultdict — less code, same structure
from collections import defaultdict

def make_node():
    return defaultdict(make_node)

root = make_node()

def insert(root, word):
    node = root
    for ch in word:
        node = node[ch]
    node['#'] = True        # '#' as end-of-word marker

def search(root, word):
    node = root
    for ch in word:
        if ch not in node: return False
        node = node[ch]
    return '#' in node

def starts_with(root, prefix):
    node = root
    for ch in prefix:
        if ch not in node: return False
        node = node[ch]
    return True
```