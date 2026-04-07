class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for num in nums:
            hash_map[num] = 1 + hash_map.get(num, 0)

        arr = []

        for key, value in hash_map.items():
            arr.append([value, key])

        arr.sort()

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])

        return res
        