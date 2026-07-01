class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        

        if not s: return 0 

        window= {}
        left = 0
        maxfrequency = 0
        maxlength = 0

        for right in range(len(s)):

            if s[right] not in window:
                window[s[right]] = 1
            else:
                window[s[right]]+=1

            maxfrequency = max(window[s[right]], maxfrequency)

            

            while (right -left +1) - maxfrequency >k:
                window[s[left]] -=1
                left +=1

            maxlength = max(maxlength, right- left+1)

            

           


        return maxlength



    

            

            

            





        