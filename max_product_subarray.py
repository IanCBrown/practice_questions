class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return
        
        if len(nums) == 1:
            return nums[0]
        
        max_prod = nums[0]
        min_prod = nums[0]
        ret = nums[0]
        
        
        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_prod, min_prod = min_prod, max_prod
            min_prod = min(nums[i], nums[i] * min_prod)
            max_prod = max(nums[i], nums[i] * max_prod)
        
            
            ret = max(ret, max_prod)
            
            
        return ret
        
        
