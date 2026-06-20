class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        convert_set = set(nums)
        longest = 0
        for num in nums: #1 100 2 200 3 4 101
            if (num - 1 not in convert_set):
                length = 0
                while (num in convert_set):
                    length += 1
                    num += 1
                longest = max(length, longest)
        return longest