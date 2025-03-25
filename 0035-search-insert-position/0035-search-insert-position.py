class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right=0,len(nums)-1
        while(left<=right):
            mid=left+((right-left)//2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        if target > nums[mid]:
            return mid+1
        elif target < nums[mid] and mid>0:
            return mid-1
        else :
            return 0
        