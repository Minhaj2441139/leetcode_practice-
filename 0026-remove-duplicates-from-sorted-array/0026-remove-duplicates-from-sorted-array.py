class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = set()
        write_pointer = 0
        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[write_pointer] = num
                write_pointer += 1
        
        return write_pointer