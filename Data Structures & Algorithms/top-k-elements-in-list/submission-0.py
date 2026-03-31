class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash_set  = {}
        
        for n in nums:
            if n in hash_set:
                hash_set[n] += 1
            else:
                hash_set[n] = 1

        return heapq.nlargest(k, hash_set, key=hash_set.get)