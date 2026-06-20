class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        hashset_s = {}
        hashset_t = {}

        for i in range(len(s)):
            if (s[i] not in hashset_s):
                hashset_s[s[i]] = 1
            elif (s[i] in hashset_s):
                hashset_s[s[i]] += 1
            if (t[i] not in hashset_t):
                hashset_t[t[i]] = 1
            elif (t[i] in hashset_t):
                hashset_t[t[i]] += 1

        if hashset_s == hashset_t:
            return True

        return False
        