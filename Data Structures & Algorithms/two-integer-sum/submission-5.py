class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        for i in range(len(nums)):
            dict_nums[nums[i]] = [i] + dict_nums.get(nums[i],[])
   
        for key, value in dict_nums.items():
            if target-key == key and len(dict_nums[key]) >1:
                ans = [dict_nums[key][0], dict_nums[key][1]]
                ans.sort()
                return ans
            elif (target- key) in dict_nums.keys():
                if value[0] != dict_nums[target-key][0]:
                    ans = [value[0], dict_nums[target-key][0]]
                    ans.sort()
                    return ans

                