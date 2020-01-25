class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = [0] * len(nums)
        R = [0] * len(nums)
        ret = [0] * len(nums)
        
        L[0] = 1
        R[len(nums) - 1] = 1
        
        for i in range(1, len(L)):
            L[i] = nums[i - 1] * L[i - 1]
            
        for i in range(len(R) - 2, -1, -1):
            R[i] = nums[i + 1] * R[i + 1]
        
        print(R)
        print(L)
        for i in range(len(nums)):
            ret[i] = L[i] * R[i]
            
        return ret


    def _productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [0] * len(nums)
        total = 1
        for num in nums:
            total *= num
        
        for i in range(len(nums)):
            ret[i] = total // nums[i]
            
        return ret

    