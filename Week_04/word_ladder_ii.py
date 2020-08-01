import collections
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def edges(word):
            for i in range(len(word)):
                for newWord in dict[word[:i] + '*' + word[i + 1:]]:
                    if not newWord in marked:
                        yield newWord

        def find_path(end):
            res = []
            for curr in end:
                for parent in path[curr[0]]:
                    res.append([parent] + curr)
            return res

        if not endWord in wordList:
            return []
        dict = collections.defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                dict[word[:i] + "*" + word[i + 1:]].append(word)

        marked = set()
        path = collections.defaultdict(set)
        begin = {beginWord}
        end = {endWord}
        forward = True
        while begin and end:
            if len(begin) > len(end):
                begin, end = end, begin
                forward = not forward
            temp = set()
            for word in begin:
                marked.add(word)
            for word in begin:
                for w in edges(word):
                    temp.add(w)
                    if forward:
                        path[w].add(word)
                    else:
                        path[word].add(w)
            begin = temp
            if begin & end:
                res = [[endWord]]
                while res[0][0] != beginWord:
                    res = find_path(res)
                return res
        return []
