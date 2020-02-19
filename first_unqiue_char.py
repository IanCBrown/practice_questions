class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 1:
            return 0
        elif len(s) == 0:
            return -1
        
        counts = {}
        for i in range(len(s)):
            if s[i] in counts:
                counts[s[i]][0] += 1 
            else:
                counts[s[i]] = [1, i]
                
        for key, value in counts.items():
            if value[0] == 1:
                return value[1]
        return -1 


def one_pass(s: str) -> int:
    if len(s) == 0:
        return -1
    visited = set()
    char_idx = {}

    for i in range(len(s)):
        if s[i] not in visited:
            visited.add(s[i])
            char_idx[s[i]] = i
        else:
            if s[i] in char_idx:
                del char_idx[s[i]]

    if len(char_idx) == 0:
        return -1
    else:
        return min(char_idx.values())
