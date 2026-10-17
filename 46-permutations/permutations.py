class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        
        def helper(remaining, curr):
            if not remaining:
                ans.append(curr[:])
            for i, digit in enumerate(remaining):
                curr.append(digit)
                helper(remaining[:i] + remaining[i+1:], curr)
                curr.pop()
        
        helper(nums, [])
        return ans