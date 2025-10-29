class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # s=list(set(nums))
        # count=[]
        # i=0
        # for x in s:
        #     for y in nums:
        #         if x==y:
        #             count[i]+=1
        #     i+=1
        # m=0
        # for z in range(len(count)):
        #     if m<count[z]:
        #         m=
        can=0
        count=0
        for x in range(len(nums)):
            if count == 0:
                can=nums[x]
                count+=1
            elif can ==nums[x]:
                count+=1
            else:
                count-=1
        return can