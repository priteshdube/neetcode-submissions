class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        result =[]

        def helper(i, temp, cursum):
            if cursum == target:
                result.append(temp[:])
                return

            if cursum > target:
                return 


            for j in range(i, len(nums)):


                temp.append(nums[j])
                helper(j, temp, cursum+ nums[j])
                temp.pop()
               


        helper(0, [], 0)

        return result
