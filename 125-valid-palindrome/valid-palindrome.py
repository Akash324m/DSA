class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp=""
        for x in s:
            if 64<ord(x)<91 or 96<ord(x)<123 or 47<ord(x)<58:
                temp=temp+x
        #print(temp)
        if len(temp)==0 or len(temp)==1:
            return True
        final=temp[::-1]
        if final.lower() == temp.lower():
            return True
        else:
            return False
        # i=0
        # j=len(temp)-1
        # for x in range(len(temp)):
        #     if i == j:
        #         return True
        #         break
        #     elif temp[i]!=temp[-(i+1)]:
        #         return False
        #     i+=1
        #     j-=1
