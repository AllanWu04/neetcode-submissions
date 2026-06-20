class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        result = []
        for i in range(len(nums)):
            result.append(pre)
            pre *= nums[i]
        print(result)
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= post
            post *= nums[i]
        return result