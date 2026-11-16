class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                
                freq[num] += 1
            else:
                freq[num] = 1
      
        maj_ele = []
        min_occ = len(nums)/3
        for key, value in freq.items():
            if value > min_occ:
                maj_ele.append(key)
        return maj_ele