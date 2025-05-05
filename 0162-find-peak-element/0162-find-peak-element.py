class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxo=max(nums)
        ind=nums.index(maxo)
        return ind