class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s) 
        if n < 2:
            return s
        
        start = 0 
        end = 0 
        for i in range(n):
            len1 = extend_palindrome(s, i, i + 1)
            len2 = extend_palindrome(s, i, i)
            ln = max(len1, len2)
            if ln > (end - start):
                start = i - (ln - 1) // 2
                end = i + (ln // 2)
                
        return s[start:end+1]
            
        
        
def extend_palindrome(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1 
        r += 1
    return r - l - 1
