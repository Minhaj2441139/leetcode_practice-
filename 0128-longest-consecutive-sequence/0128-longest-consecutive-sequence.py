class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        nums.sort()
        count=1
        maxi=1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i]==nums[i-1]+1:
                count+=1
                maxi=max(maxi,count)
            else:
                count=1

        return maxi