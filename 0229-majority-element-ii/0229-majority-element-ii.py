class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a=Counter(nums)
        res=[]
        for num,count in a.items():
            if count>len(nums)//3:
                res.append(num)
        
        return res
