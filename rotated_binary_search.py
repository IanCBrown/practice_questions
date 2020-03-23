class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1 
        elif len(nums) == 1 and nums[0] == target:
            return 0
        elif len(nums) == 1:
            return -1
        
        pivot = nums.index(min(nums))
        ret = -1 
        
        if pivot == 0:
            ret = self.binary_search(nums, target)
        elif target < nums[0]:
            ret = self.binary_search(nums[pivot:], target)
            if ret != -1:
                ret += pivot
        else:
            ret = self.binary_search(nums[0:pivot], target)
            
        return ret
    
    def binary_search(self, nums, target):
        mini = 0 
        maxi = len(nums) - 1
        
        while mini <= maxi:
            guess = (mini + maxi) // 2
            if nums[guess] == target:
                return guess
            elif nums[guess] > target:
                maxi = guess - 1
            else:
                mini = guess + 1
                
        return -1
