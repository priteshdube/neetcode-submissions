class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []

        def helper(temp,i):
            result.append(temp[:])

            for j in range(i, len(nums)):

                temp.append(nums[j])
                helper(temp, j+1)
                temp.pop()


        helper([], 0)

        return result
        