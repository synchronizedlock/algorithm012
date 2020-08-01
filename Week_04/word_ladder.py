from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, word_set: List[str]) -> int:
        word_set = set(word_set)
        if endWord not in word_set:
            return 0
        if beginWord in word_set:
            word_set.remove(beginWord)

        res, forward, backward = 2, {beginWord}, {endWord}
        letters, length = set('qwertyuioplkjhgfdsazxcvbnm'), len(endWord)
        while forward:
            if len(forward) > len(backward):
                forward, backward = backward, forward

            cur = set()
            for word in forward:
                for idx in range(length):
                    x, y = word[:idx], word[idx + 1:]
                    for letter in letters:
                        temp = x + letter + y
                        if temp in backward: return res
                        if temp in word_set:
                            cur.add(temp)
                            word_set.remove(temp)
            res += 1
            forward = cur
        return 0
