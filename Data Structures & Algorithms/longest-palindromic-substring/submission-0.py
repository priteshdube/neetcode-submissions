class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s

        def helper(left, right):

            while left>= 0 and right <= len(s)-1 and s[left] == s[right]:
                
                left -=1
                right +=1

            return right - left -1

        

        maxlen = 0
        start = 0

        for i in range(len(s)):
            #odd length 

            l1 = helper(i, i)

            #even length
            l2 = helper(i, i+1)

            cmax= max(l1, l2)

            if cmax > maxlen:
                maxlen= cmax

                start = i - (cmax -1)//2


        return s[start: start + maxlen]

