class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashset = {}
        freq = [[] for i in range(len(nums) + 1)] #Num buckets (add 1 so that we can ignore 0 idx)


        for num in nums:
            if num in hashset:
                hashset[num] += 1
            else:
                hashset[num] = 1
        
        for num, cnt in hashset.items(): #We append bucket according to total num appearances
            freq[cnt].append(num)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]: #Up to k times which is constant
                res.append(num)
                if (len(res) == k):
                    return res