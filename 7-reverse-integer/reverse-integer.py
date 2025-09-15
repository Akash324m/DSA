class Solution:
    def reverse(self, x: int) -> int:
        arr=[]
        if x<0:
            sign = "m"
        else:
            sign = "p"
        x = abs(x)
        while(x>0):
            rem = x%10
            arr.append(rem)
            x = x//10
        arr = arr[::-1]
        s = 0
        for i in range(len(arr)):
            s += arr[i]*(10**i)
        if sign == "m":
            s = s - (2*s)
        if -2147483648 < s and s < 2147483648:
            return s
        else:
            return 0

        