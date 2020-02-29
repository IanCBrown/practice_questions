class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        
        count = 0
        ret = []
        for i, sym in enumerate(S):
            if sym == "(":
                if count != 0:
                    ret.append("(")
                count += 1
            else:
                count -= 1
                if count != 0:
                    ret.append(")")
        return "".join(ret)
