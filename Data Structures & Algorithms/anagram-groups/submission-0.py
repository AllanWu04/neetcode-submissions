class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset = defaultdict(list)
        for s in strs: #Iterate through list
            key = [0] * 26
            for c in s: #Iterate through strings
                key[ord(c) - ord('a')] += 1 #Ascii subtraction to generate key for anagrams
            hashset[tuple(key)].append(s)

        return list(hashset.values())