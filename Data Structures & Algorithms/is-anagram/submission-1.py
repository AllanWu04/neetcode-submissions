class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashset_s = {}
        hashset_t = {}
        for idx in range(len(s)):
            if s[idx] in hashset_s:
                hashset_s[s[idx]] += 1
            else:
                hashset_s[s[idx]] = 1
            if t[idx] in hashset_t:
                hashset_t[t[idx]] += 1
            else:
                hashset_t[t[idx]] = 1
        
        if hashset_s == hashset_t:
            return True
        return False
        