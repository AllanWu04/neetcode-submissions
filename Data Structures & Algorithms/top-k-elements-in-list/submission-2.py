class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashset = {}
        freq = [[] for i in range(len(nums) + 1)] #Total Buckets

        for num in nums:
            if (num in hashset):
                hashset[num] += 1
            else:
                hashset[num] = 1

        for num, cnt in hashset.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if (len(res) == k):
                    return res