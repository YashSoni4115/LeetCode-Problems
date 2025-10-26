"""
------------------------------------------------------------
LeetCode 152, Maximum Product Subarray, difficulty medium, language python
Saved at 2025-10-26 13:36:34
------------------------------------------------------------
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def product(sub):
            prod = 1
            for num in sub:
                prod *= num
            return prod

        max_prd = nums[0]

        divided = []
        curr = []

        for num in nums:
            if num != 0:
                curr.append(num)
            else:
                max_prd = max(0, max_prd)
                if curr != []: divided.append(curr)
                curr = []
                if len(nums) == 1:
                    return 0
        if curr != []: divided.append(curr)

        for subarray in divided:
            
            neg_count = 0
            indexes = []

            print(subarray)

            if len(subarray) == 1:
                max_prd = max(subarray[0], max_prd)
                continue

            for i, num in enumerate(subarray):
                if num < 0:
                    neg_count += 1
                    indexes.append(i)
                
            if neg_count % 2 == 0:
                max_prd = max(product(subarray), max_prd)
            else:
                left = product(subarray[:indexes[-1]])
                right = product(subarray[indexes[0] + 1:])
                max_prd = max(max(left, right), max_prd)

        return max_prd
