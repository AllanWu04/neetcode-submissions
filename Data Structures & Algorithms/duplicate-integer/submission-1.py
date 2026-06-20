class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        remove_dupes = set()
        for num in nums:
            if num in remove_dupes:
                return True
            remove_dupes.add(num)
        return False