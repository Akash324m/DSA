class Solution(object):
    def removeDuplicates(self,nums):
        expectedNums = list(set(nums))
        expectedNums.sort()
        for x in range(len(expectedNums)):
            nums[x]=expectedNums[x]
        print(nums)
        print(expectedNums)
        return len(expectedNums)


        

    