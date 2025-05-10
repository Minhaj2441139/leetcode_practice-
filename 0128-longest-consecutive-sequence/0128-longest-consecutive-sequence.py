class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsS=set(nums)
        maxi=0
        for num in numsS:
            if num-1 not in numsS:
                count=0
                while num+count in numsS:
                    count+=1
                    maxi=max(maxi,count)
        return maxi