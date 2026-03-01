# 🌳 Trees

> Master DFS (recursion) and BFS (queue). Nearly every tree problem is a variant of one of these two.

---

## Patterns Overview

| Pattern | When to Use | Key Idea |
|---------|------------|---------|
| [DFS — Recursive](#-dfs--recursive) | Paths, heights, subtree checks, LCA | What does the function return at each node? |
| [BFS — Level Order](#-bfs--level-order) | Level-by-level, right side view, width | Queue — process all nodes per level |
| [BST Properties](#-bst-properties) | Leverage left < root < right rule | In-order traversal gives sorted sequence |
| [Tree Construction](#-tree-construction) | Build from traversal arrays | Pre/Post gives root; In-order splits left/right |

---

## Node Definition

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

---

## 🔁 DFS — Recursive

**When to use:** Path problems, heights, subtree checks, lowest common ancestor.

**The key question to ask:** *What should this function return at each node?*

**Trigger keywords:** "path sum", "height", "depth", "diameter", "subtree", "LCA", "max path"

```python
# Maximum depth
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

# Path Sum II — all root-to-leaf paths that sum to target
def path_sum(root, target):
    result = []

    def dfs(node, remaining, path):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right and remaining == node.val:
            result.append(list(path))   # copy!
        dfs(node.left, remaining - node.val, path)
        dfs(node.right, remaining - node.val, path)
        path.pop()   # backtrack

    dfs(root, target, [])
    return result

# Diameter — left_height + right_height at each node
def diameter_of_binary_tree(root):
    diameter = [0]

    def height(node):
        if not node:
            return 0
        left_h = height(node.left)
        right_h = height(node.right)
        diameter[0] = max(diameter[0], left_h + right_h)
        return 1 + max(left_h, right_h)

    height(root)
    return diameter[0]

# Max Path Sum — return only single branch upward, track global max
def max_path_sum(root):
    max_sum = [float('-inf')]

    def dfs(node):
        if not node:
            return 0
        left  = max(dfs(node.left), 0)    # ignore negative paths
        right = max(dfs(node.right), 0)
        max_sum[0] = max(max_sum[0], node.val + left + right)
        return node.val + max(left, right) # return single branch only

    dfs(root)
    return max_sum[0]
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Maximum Depth of Binary Tree | #104 | 🟢 Easy | `1 + max(left_depth, right_depth)` |
| Invert Binary Tree | #226 | 🟢 Easy | Swap left and right children recursively |
| Symmetric Tree | #101 | 🟢 Easy | Mirror check — compare opposite subtrees |
| Path Sum | #112 | 🟢 Easy | Subtract node value going down, check at leaf |
| Path Sum II — all paths | #113 | 🟡 Medium | Backtrack — append on enter, pop on exit |
| Diameter of Binary Tree | #543 | 🟢 Easy | `left_height + right_height` at each node |
| Binary Tree Max Path Sum | #124 | 🔴 Hard | Track global max; return only single branch up |

---

## 🌊 BFS — Level Order

**When to use:** Level-by-level processing, right side view, minimum depth, width-based measurements.

**Trigger keywords:** "level order", "right side view", "average per level", "minimum depth", "zigzag"

```python
from collections import deque

# Level order traversal
def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):   # process exactly this level
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)

    return result

# Right Side View — last node at each level
def right_side_view(root):
    result = []
    queue = deque([root]) if root else deque()

    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if i == len(queue):     # last node in this level
                result.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)

    return result
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Binary Tree Level Order Traversal | #102 | 🟡 Medium | deque — process all nodes per level |
| Binary Tree Right Side View | #199 | 🟡 Medium | Capture the last node at each BFS level |
| Average of Levels in Binary Tree | #637 | 🟢 Easy | Sum / count at each level |
| Maximum Width of Binary Tree | #662 | 🟡 Medium | Track column indices with each node |
| Minimum Depth | #111 | 🟢 Easy | BFS — return depth at first leaf reached |
| Zigzag Level Order Traversal | #103 | 🟡 Medium | Alternate left-right direction each level |

---

## 🌲 BST Properties

**When to use:** Leverage BST rule — `left < root < right`. In-order traversal of a BST yields a sorted sequence.

**Trigger keywords:** "validate BST", "kth smallest", "in-order", "binary search tree"

```python
# Validate BST — pass min/max bounds down
def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    if root.val <= min_val or root.val >= max_val:
        return False
    return (is_valid_bst(root.left, min_val, root.val) and
            is_valid_bst(root.right, root.val, max_val))

# Kth Smallest — in-order traversal
def kth_smallest(root, k):
    stack = []
    curr = root
    count = 0

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        count += 1
        if count == k:
            return curr.val
        curr = curr.right

# Lowest Common Ancestor of BST
def lowest_common_ancestor(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root   # root is between p and q
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Validate BST | #98 | 🟡 Medium | Pass `(min_bound, max_bound)` down recursively |
| Kth Smallest Element in a BST | #230 | 🟡 Medium | In-order traversal, decrement counter k |
| Lowest Common Ancestor of BST | #235 | 🟢 Easy | Both > root → right; else → left |
| Insert into a BST | #701 | 🟡 Medium | Recurse to the correct leaf position |
| Delete Node in a BST | #450 | 🟡 Medium | 3 cases: leaf / one child / two children |

---

## 🏗️ Tree Construction

**When to use:** Build a tree from traversal arrays.

**Key rule:**
- **Preorder** first element = root → remaining split by inorder
- **Postorder** last element = root → remaining split by inorder
- **Inorder** left of root = left subtree, right of root = right subtree

```python
# Build from Preorder + Inorder
def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)
    mid = inorder.index(root_val)   # split point in inorder

    root.left  = build_tree(preorder[1:mid+1], inorder[:mid])
    root.right = build_tree(preorder[mid+1:],  inorder[mid+1:])
    return root

# Serialize / Deserialize
def serialize(root):
    if not root:
        return "N"
    return f"{root.val},{serialize(root.left)},{serialize(root.right)}"

def deserialize(data):
    vals = iter(data.split(','))

    def dfs():
        val = next(vals)
        if val == "N":
            return None
        node = TreeNode(int(val))
        node.left  = dfs()
        node.right = dfs()
        return node

    return dfs()
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Build Tree from Preorder + Inorder | #105 | 🟡 Medium | `preorder[0]` = root, split inorder around it |
| Build Tree from Inorder + Postorder | #106 | 🟡 Medium | `postorder[-1]` = root, split inorder |
| Serialize and Deserialize Binary Tree | #297 | 🔴 Hard | BFS or DFS with null markers |
| Construct BST from Preorder | #1008 | 🟡 Medium | Use BST property to place each node |

---

## 🔀 Combined Practice

> These problems require mixing 2+ patterns. Spend 15+ minutes before checking hints.

| Problem | LC # | Difficulty | Patterns Required |
|---------|------|-----------|------------------|
| Binary Tree Cameras | #968 | 🔴 Hard | DFS post-order + greedy camera placement |
| Path Sum III — any path | #437 | 🟡 Medium | DFS + prefix sum hashmap |
| All Nodes Distance K in BT | #863 | 🟡 Medium | BFS from target + parent pointer mapping |
| Vertical Order Traversal | #987 | 🔴 Hard | BFS + sort by (column, row, value) |
| Count Good Nodes in BT | #1448 | 🟡 Medium | DFS — pass max seen on current path |
| Maximum Sum BST in BT | #1373 | 🔴 Hard | DFS returning `(isValid, min, max, sum)` |

---

## 📚 Resources

| Resource | Link | Best For |
|----------|------|---------|
| NeetCode Trees Playlist | youtube.com/@NeetCode | DFS and BFS patterns with clean Python |
| VisuAlgo BST | visualgo.net/en/bst | Animate insert, delete, and search on BST |
| LeetCode Explore — Binary Tree | leetcode.com/explore/learn/card/data-structure-tree | Official structured card |
| Striver Tree Series | takeuforward.org | Most thorough tree coverage available |

---

## 🐍 Python Tips

```python
# DFS iterative (pre-order) using stack
stack = [root]
while stack:
    node = stack.pop()
    if not node: continue
    # process node
    stack.append(node.right)   # push right first
    stack.append(node.left)    # so left is processed first

# In-order iterative
stack, curr = [], root
while curr or stack:
    while curr:
        stack.append(curr)
        curr = curr.left
    curr = stack.pop()
    # process curr
    curr = curr.right

# BFS skeleton
from collections import deque
q = deque([root])
while q:
    node = q.popleft()
    if node.left:  q.append(node.left)
    if node.right: q.append(node.right)
```