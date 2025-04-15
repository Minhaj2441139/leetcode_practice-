class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0]
        for n in nums:
            self.sums.append(self.sums[-1] + n)
        self.sums = self.sums[1:]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]
        else:
            return self.sums[right] - self.sums[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)