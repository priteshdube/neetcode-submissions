class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s: return 0 
        if len(s) ==1: return 1 



        # function

        left_pointer = 0 
        longest= 1
        window = set()

        for right_pointer in range(len(s)):

            while s[right_pointer] in window:
                window.remove(s[left_pointer])
                left_pointer +=1

            window.add(s[right_pointer])

            current = right_pointer - left_pointer+1

            longest = max(current, longest)


        return longest

        