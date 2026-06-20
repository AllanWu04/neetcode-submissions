class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, a in enumerate(nums):

            if a > 0: 
                break

            if (i > 0 and nums[i - 1] == a): #If the number before is the same, go next since it will give dupe result set
                continue

            left_ptr, right_ptr = i + 1, len(nums) - 1
            while (left_ptr < right_ptr):
                three_sum = a + nums[left_ptr] + nums[right_ptr]
                if three_sum == 0:
                    result.append([a, nums[left_ptr], nums[right_ptr]])
                    left_ptr += 1
                    right_ptr -= 1
                    while (nums[left_ptr] == nums[left_ptr - 1] and left_ptr < right_ptr):
                        left_ptr += 1
                elif three_sum > 0:
                    right_ptr -= 1
                elif three_sum < 0:
                    left_ptr += 1

        return result