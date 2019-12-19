class Solution:
    def longestCommonPrefix(self, strs):
        strs.sort()
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        
        len_shortest = float('inf')
        for st in strs:
            if len(st) == 0:
                return ""
            elif len(st) < len_shortest:
                len_shortest = len(st)
            
        index = -1
        ret = []
        
        while True:
            index += 1
            if index < len_shortest:       
                curr = strs[0][index]
                for i in range(len(strs)):
                    if strs[i][index] != curr:
                        return "".join(ret)
                    elif i == len(strs) - 1:
                        ret.append(strs[i][index])
            else:
                break
        return "".join(ret)         
            