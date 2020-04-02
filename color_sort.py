import collections 

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = collections.Counter(nums)
        # update values so we can use them in the following loop
        c[1] += c[0]
        c[2] += c[1]
        for i in range(len(nums)):
            if i < c[0]:
                nums[i] = 0
            elif i < c[1]:
                nums[i] = 1
            else:
                nums[i] = 2
