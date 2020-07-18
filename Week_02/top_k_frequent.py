from typing import List
from collections import Counter
import heapq as hq


class Solution:
    def topKFrequent_simple(self, nums: List[int], k: int) -> List[int]:
        return [i[0] for i in Counter(nums).most_common(k)]

    def topKFrequent_heapq(self, nums: List[int], k: int) -> List[int]:
        lookup = Counter(nums)
        res, heap = [], []
        for num, freq in lookup.items():
            if len(heap) == k:
                if heap[0][0] < freq:
                    hq.heapreplace(heap, (freq, num))
            else:
                hq.heappush(heap, (freq, num))
        while heap:
            res.append(hq.heappop(heap)[1])

        return res
