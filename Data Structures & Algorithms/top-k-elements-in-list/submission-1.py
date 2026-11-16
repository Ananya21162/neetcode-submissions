class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num,0)+1
        ans = []
        for num, _ in sorted(freqMap.items(), key= lambda item : item[1], reverse = True):
            if k > 0:
                ans.append(num)
                k -= 1
            else:
                break
        return ans

            
        