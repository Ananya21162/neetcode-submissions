class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict_idx = {}
        for i in range(len(numbers)):
            dict_idx[numbers[i]] = i
        for i in range(len(numbers)):
            y = target - numbers[i]
            if y in dict_idx.keys() and i != dict_idx[y]:
                return [i+1, dict_idx[y]+1]
            
        
