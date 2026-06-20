class Solution:
    def maxArea(self, heights: List[int]) -> int:

        length = len(heights) - 1
        left_ptr, right_ptr = 0, length
        max_water = 0

        while (left_ptr < right_ptr):
            get_area = min(heights[left_ptr], heights[right_ptr]) * length
            max_water = max(max_water, get_area)
            if (heights[left_ptr] < heights[right_ptr]):
                left_ptr += 1
            else:
                right_ptr -= 1
            length -= 1

        return max_water