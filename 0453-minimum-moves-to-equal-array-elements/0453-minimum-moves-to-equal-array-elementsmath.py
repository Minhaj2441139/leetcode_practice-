class Solution:
    def minMoves(self, nums: List[int]) -> int:
        steps = 0
        min_num = min(nums)
        for num in nums:
            steps += abs(min_num - num)
        return steps