class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        for x in range(len(nums)+1):
            if x not in nums:
                return x