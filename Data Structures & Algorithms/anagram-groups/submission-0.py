class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Create a dict with keys as array of char freq and values as strings
        response = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            response[tuple(count)].append(s)
        return response.values()


        