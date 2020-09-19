##### 毕业总结
##### 算法模板
+ 前中后序遍历
```python
def preorder(self, root):
    if root:
        self.traverse_path.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

def inorder(self, root):
    if root:
        self.inorder(root.left)
        self.traverse_path.append(root.val)
        self.inorder(root.right)

def postorder(self, root):
    if root:
        self.postorder(root.left)
        self.postorder(root.right)
        self.traverse_path.append(root.val)
```

+ 递归
```python
def recursion(level, param1, param2, ...):
    # recursion terminator
    if level > MAX_LEVEL:
        process_result
        return
    
    # process logic in current level
    process(level, data)
    
    # drill down
    self.recursion(level+1, p1, p2, ...)

    # reverse the current level status if need
```

+ 分治
```python
def divide_conquer(problem, param1, param2, ...):
    # recursion terminator
    if problem is None:
        print result
        return

    # prepare data
    data = prepare_data(problem)
    sub_problems = split_problem(problem)
    
    # conquer sub-problems
    sub_result_1 = self.divide_conquer(sub_problems[0], p1, p2, ...)
    sub_result_2 = self.divide_conquer(sub_problems[1], p1, p2, ...)
    sub_result_3 = self.divide_conquer(sub_problems[2], p1, p2, ...)
    ...

    # process and generate final result
    result = process_result(sub_result_1, sub_result_2, sub_result_3, ...)

    # revert the current level status if need
```

+ DFS
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
+ BFS
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
+ 双向BFS
```python
front, back = [begin_node], [end_node]
level, visited = 0, []
while front and back: 
    level += 1 
    next_front = []

    for node in front: 
        if node in back: 
            return
        if node not in visited:
            visited.append(node) 
            next_front.append(node) 
            
            front = next_front

    if len(front) > len(back): 
        front, back = back, front 
        return
```
+ 二分查找
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
+ Trie树
```python
class Trie(object):
  
	def __init__(self): 
		self.root = {} 
		self.end_of_word = "#" 
 
	def insert(self, word): 
		node = self.root 
		for char in word: 
			node = node.setdefault(char, {}) 
		node[self.end_of_word] = self.end_of_word 
 
	def search(self, word): 
		node = self.root 
		for char in word: 
			if char not in node: 
				return False 
			node = node[char] 
		return self.end_of_word in node 
 
	def startsWith(self, prefix): 
		node = self.root 
		for char in prefix: 
			if char not in node: 
				return False 
			node = node[char] 
		return True
```
+ 并查集
```python
def init(p): 
	# for i = 0 .. n: p[i] = i; 
	p = [i for i in range(n)] 
 
def union(self, p, i, j): 
	p1 = self.parent(p, i) 
	p2 = self.parent(p, j) 
	p[p1] = p2 
 
def parent(self, p, i): 
	root = i 
	while p[root] != root: 
		root = p[root] 
	while p[i] != i: # 路径压缩 ?
		x = i; i = p[i]; p[x] = root 
	return root
```
+ A*
```python
def AstarSearch(graph, start, end):
	pq = collections.priority_queue() # 优先级 —> 估价函数
	pq.append([start]) 
	visited.add(start)

	while pq: 
		node = pq.pop() # can we add more intelligence here ?
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node)

    unvisited = [node for node in nodes if node not in visited]
	pq.push(unvisited)
```
+ BloomFilter
```python
from bitarray import bitarray 
import mmh3 
class BloomFilter: 
	def __init__(self, size, hash_num): 
		self.size = size 
		self.hash_num = hash_num 
		self.bit_array = bitarray(size) 
		self.bit_array.setall(0) 
	def add(self, s): 
		for seed in range(self.hash_num): 
			result = mmh3.hash(s, seed) % self.size 
			self.bit_array[result] = 1 
	def lookup(self, s): 
		for seed in range(self.hash_num): 
			result = mmh3.hash(s, seed) % self.size 
			if self.bit_array[result] == 0: 
				return "Nope" 
		return "Probably" 
bf = BloomFilter(500000, 7) 
bf.add("dantezhao") 
print (bf.lookup("dantezhao")) 
print (bf.lookup("yyj")) 
```
+ LRU cache
```python
class LRUCache(object): 
	def __init__(self, capacity): 
		self.dic = collections.OrderedDict() 
		self.remain = capacity

	def get(self, key): 
		if key not in self.dic: 
			return -1 
		v = self.dic.pop(key) 
		self.dic[key] = v   # key as the newest one 
		return v 

	def put(self, key, value): 
		if key in self.dic: 
			self.dic.pop(key) 
		else: 
			if self.remain > 0: 
				self.remain -= 1 
			else:   # self.dic is full
				self.dic.popitem(last=False) 
		self.dic[key] = value
```
