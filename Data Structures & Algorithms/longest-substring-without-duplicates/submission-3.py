class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set() #Tracks what chars have been seen
        left_ptr = 0 #Increases when duplicate is found since the next sub can be larger
        count = 0 #Get Longest so track

        for right_ptr in range(len(s)):
            while s[right_ptr] in window: #Only continues while on duplicate character
                window.remove(s[left_ptr])
                left_ptr += 1
            window.add(s[right_ptr])
            count = max(count, right_ptr - left_ptr + 1)

        return count