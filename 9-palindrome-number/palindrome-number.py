class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            s = str(x)
            n = len(s)
            rs = s[::-1]
            if rs==s:
                return True
            else:
                return False