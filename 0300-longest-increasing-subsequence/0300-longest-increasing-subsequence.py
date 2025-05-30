class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp = [1] * n  # Each element is at least a subsequence of length 1

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
