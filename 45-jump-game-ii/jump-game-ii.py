class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [float('inf')]*(n)
        dp[0] = 0
        for i in range(n):
            if nums[i] == 0: pass
            for j in range(1, nums[i]+1):
                if i + j >= n:
                    break
                dp[i+j] = min(dp[i+j], dp[i] + 1)
        return dp[-1]