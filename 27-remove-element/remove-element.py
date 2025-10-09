class Solution(object):
    def removeElement(self, nums, val):
        while True:
            if val in nums:
                res = nums.remove(val)
            else:
                break
        return len(nums)
        