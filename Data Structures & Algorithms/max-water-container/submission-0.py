class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left_ptr, right_ptr = 0, len(heights) - 1
        result = 0

        while(left_ptr < right_ptr):

            total_area = (right_ptr - left_ptr) * min(heights[left_ptr], heights[right_ptr])
            result = max(result, total_area)

            if (heights[left_ptr] <= heights[right_ptr]):
                left_ptr += 1
                
            elif (heights[left_ptr] > heights[right_ptr]):
                right_ptr -= 1

        return result