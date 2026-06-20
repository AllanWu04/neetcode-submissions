class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashset={} #This makes a map to count occurrences (key=num:value=num_occurrences)
        occur = [] #This makes buckets to act as keys for num_occurrences

        #This for-loop initializes empty buckets
        for bucket in range(len(nums) + 1):
            occur.append([])

        #This for-loop counts the occurrences of numbers and stores in hashset
        for num in nums:
            hashset[num] = 1 + hashset.get(num, 0)
        
        #This for-loop iterates key-value of hashset to search bucket of that occurrence and add num to it
        for num, c in hashset.items():
            occur[c].append(num)

        result = []
        #This for-loop reverse loops through the 2d occur array then stores in result most occur up to k
        for i in range(len(occur) - 1, 0, -1):
            for num in occur[i]:
                result.append(num)
                if len(result) == k:
                    return result
                