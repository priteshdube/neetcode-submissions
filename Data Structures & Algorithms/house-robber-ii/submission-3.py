class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)<=2: return max(nums)

        def helper(arr):

            dp= [0] * (len(arr))

            dp[0]= arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2,len(arr)):
                dp[i] = max(dp[i-1], arr[i]+ dp[i-2])

            return dp[-1]

        arr1= nums[:-1]
        arr2 = nums[1:]

        mx1 = helper(arr1)
        mx2= helper(arr2)

        return max(mx1, mx2)

        

        