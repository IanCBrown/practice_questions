class Solution:
    def longestConsecutive(self, nums):
        seq_length = 1
        
        if len(nums) == 0:
            return 0
    
        nums.sort()
        print(nums)
        seqs = []
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i] + 1:
                seq_length += 1
            elif nums[i + 1] == nums[i]:
                continue
            else:
                seqs.append(seq_length)
                seq_length = 1   
                
        seqs.append(seq_length)
        return (max(seqs))