from typing import List


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []

        def dfs(node, depth):
            if not node:
                return
            if len(res) <= depth:
                res.append([])
            res[depth].append(node.val)
            for ch in node.children:
                dfs(ch, depth + 1)

        dfs(root, 0)
        return res
