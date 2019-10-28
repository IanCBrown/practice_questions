class Solution:
    def sortArrayByParity(self, A):
        if len(A) <= 1:
            return A
        
        even_count = 0 
        for num in A:
            if num % 2 == 0:
                even_count += 1
                
        i = 0 
        j = even_count - 1
        
        while i < even_count:
            # if both even
            if A[i] % 2 == 0 and A[j] % 2 == 0:
                i += 1
            elif A[i] % 2 != 0 and A[j] % 2 == 0:
                # swap
                A[i], A[j] = A[j], A[i]
                i += 1 
                j += 1
            elif A[i] % 2 == 0:
                i += 1
            else:
                j += 1
        
        return A