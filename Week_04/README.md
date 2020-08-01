#### 学习笔记
##### dfs
```python
def dfs(node):
    if node in visited:
        # already visited
        return

    visited.add(node)

    # process current node
    # ... logic here
    dfs(node.left)
    dfs(node.right)

visited = set()
def dfs_recursion(node, visited):
    if node in visited:
        return 

    visited.add(node)

    # process current node here
    ...
    for next_node in node.children():
        if not next_node in visited:
            dfs_recursion(next_node, visited)

def dfs_stack(self, tree):
    if tree.root is None:
        return []

    visited, stack = [], [tree.root]
    while stack:
        node = stack.pop()
        visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        stack.push(nodes)

        # other processing work
        ...
```
##### bfs
```python
def bfs(graph, start, end):
    queue = []
    queue.append([start])

    visited = []
    visited.add(start)
    
    while queue:
        node = queue.pop()
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)

        # other processing work
        ...
```
##### binary_search
```python
def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) / 2
        if array[mid] == target:
            # break or return result
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
```