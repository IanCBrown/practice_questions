class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        
        for num in nums: 
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        ret = []
        j = 0
        for i in sorted(counts.items(), key=lambda item: item[1], reverse=True):
            if j < k:
                ret.append(i[0])
                j += 1
                
        return ret
      
