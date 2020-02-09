class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        length = len(A)
        odds = []
        evens = []
        ret = [0] * length
        
        for i in range(length):
            if A[i] % 2 == 0:
                evens.append(A[i])
            elif A[i] % 2 != 0:
                odds.append(A[i])
                
        for i in range(length):
            if i % 2 == 0:
                ret[i] = evens.pop()
            else:
                ret[i] = odds.pop()
        
        return ret
            