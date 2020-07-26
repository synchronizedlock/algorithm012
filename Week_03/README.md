#### 学习笔记
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

+ 递归模版
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

+ 分治模板
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