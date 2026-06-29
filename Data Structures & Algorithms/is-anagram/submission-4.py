class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if (len(s) != len(t)):
            return False

        hashset_t = {}
        hashset_s = {}

        for char in t:
            if (char in hashset_t):
                hashset_t[char] += 1
            elif (char not in hashset_t):
                hashset_t[char] = 1
        for char in s:
            if (char in hashset_s):
                hashset_s[char] += 1
            elif (char not in hashset_s):
                hashset_s[char] = 1

        return hashset_s == hashset_t
            
        