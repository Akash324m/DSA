class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #arr = []
        # m=len(nums)+1
        # for i in range(1,m):
        #     arr.append(i)
        # result=[]
        # for x in range(1,len(nums)+1):
        #     if x not in nums:
        #         result.append(x)
        # return result
        arr = set(list([i for i in range(1,len(nums)+1)]))
        nums= set(nums)
        result = list(arr.difference(nums))
        return result
