class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = [-stone for stone in stones]
        heapq.heapify(q)
        while (len(q)) > 1:
            heapq.heappush(q, heapq.heappop(q) - heapq.heappop(q))
        return -q[0]