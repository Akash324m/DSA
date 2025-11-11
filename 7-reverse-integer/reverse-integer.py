class Solution(object):
    def reverse(self, x):
        n=False
        if x<0:
            n=True
        r=int((str(abs(x)))[::-1])
        print(r)
        if -2147483648 < r and r < 2147483647:
            if n==True:
                return -r
            else:
                return r
        else:
            return 0

        