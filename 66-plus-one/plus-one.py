class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        i=len(digits)-1
        for x in digits:
            num+=x*(10**i)
            i-=1
        num=num+1
        s=str(num)
        temp=[]
        for y in s:
            temp.append(int(y))
        return temp
