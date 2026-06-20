class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}

        for idx, val in enumerate(nums):
            hashset[val] = idx

        for idx, val in enumerate(nums):
            difference = target - val
            if difference in hashset and hashset[difference] != idx:
                return [idx, hashset[difference]]
            




        
