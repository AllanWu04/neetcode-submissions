class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_set = set()

        for i in nums:
            if i not in new_set:
                new_set.add(i)
            else:
                return True

        return False