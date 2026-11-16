class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            count = [0]*26
            for char in s:
                count[ord(char)-ord('a')] += 1

            result[tuple(count)] = result.get(tuple(count), []) + [s]
        return list(result.values())