class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for _ in range(len(nums)+1)]
        freq = defaultdict(int)
        print(count)
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        for value, occ in freq.items():
            count[occ].append(value)
        top_k =[]
        for i in reversed(range(len(count))):
            top_k.extend(count[i])
            if len(top_k)==k:
                break

        return top_k
            
        