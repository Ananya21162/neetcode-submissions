class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        responses = defaultdict(list)
        for s in strs:
            count = [0]* 26
            for ch in s:
                count[ord(ch)-ord('a')] += 1
            responses[tuple(count)].append(s)
        return list(responses.values())

