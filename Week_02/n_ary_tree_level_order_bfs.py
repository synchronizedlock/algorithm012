from typing import List


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        res = []

        def bfs(node):
            queue = [node]
            while queue:
                next = []
                tmp = []
                for node in queue:
                    tmp.append(node.val)
                    for ch in node.children:
                        next.append(ch)
                res.append(tmp)
                queue = next

        bfs(root)
        return res
