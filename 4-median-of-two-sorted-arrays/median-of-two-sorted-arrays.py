class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for x in nums2:
            nums1.append(x)
        nums1.sort()
        n=len(nums1)
        if n%2==0:
            return ( nums1[n//2] + nums1[(n//2)-1] ) / 2
        else:
            return nums1[n//2]
        