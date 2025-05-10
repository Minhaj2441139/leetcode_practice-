class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:  # Handle empty array
            return 0
        if len(nums) == 1:  # Handle single element
            return 1
        
        nums.sort()  # Sort the array (O(n log n))
        count = 1  # Current sequence length
        best = 1  # Maximum sequence length
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue  # Skip duplicates
            elif nums[i] == nums[i-1] + 1:
                count += 1  # Increment current sequence length
                best = max(best, count)  # Update maximum
            else:
                count = 1  # Reset current sequence for a new sequence
        
        return best