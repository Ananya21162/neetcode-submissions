class Solution:
  
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        length = sum(nums)//k
        if length != sum(nums)/k:
            return False
        
        nums.sort(reverse = True)
        if nums[0] > length:
            return False
        
        chosen = [False]*len(nums)
        def backtrack(i,k,subSum):
            if k == 0:
                return True
            if subSum == length:
                return backtrack(0,k-1,0)
            
            for j in range(i, len(nums)):
                if chosen[j] or subSum+nums[j] > length:
                    continue
                chosen[j] = True
                if backtrack(j,k,subSum+nums[j]):
                    return True
                chosen[j] = False
            return False
        return backtrack(0,k,0)
        