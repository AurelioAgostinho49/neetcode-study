class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_set = {}

        for str in strs:
            str_sorted = "".join(sorted(str))

            if str_sorted in hash_set:
                hash_set[str_sorted].append(str)
            else:
                hash_set[str_sorted] = [str]
        
        return list(hash_set.values())
