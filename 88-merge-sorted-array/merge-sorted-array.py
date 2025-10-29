class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m==0:
            if n==0:
                return
            for i in range(n):
                nums1[i] = nums2[i]
            return
        elif m>0 and n==0:
            return
        
        for j in range(n):
            nums1.pop(-1)

        for x in nums2:
            nums1.insert(m-1,x)
        nums1.sort()
        print(nums1)


        # x=0
        # y=0
        # temp=0
        # for i in range(m):
        #     for j in range(n):
        #         if x==m or y==n:
        #             temp=i
        #             print(i)
        #             break
        #         if nums1[x]>nums2[y]:
        #             nums1.insert(x,nums2[y])
        #     # elif nums1[x]<nums2[y]:
        #     #     nums1.insert(x,nums2[y])
        #     # if x==y :
        #     #     x+=1
        #     #     continue
        #     # if y!=n:
        #     #     y+=1


        