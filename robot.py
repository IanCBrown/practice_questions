# https://leetcode.com/problems/robot-return-to-origin/submissions/
class Solution:
    def judgeCircle(self, moves):
        pos = [0,0] 
        
        # if U += 1
        # if D -= 1
        # if R += 1
        # if L -= 1
        for move in moves:
            if move == "U":
                pos[1] += 1
            elif move == "D":
                pos[1] -= 1
            elif move == "R":
                pos[0] += 1
            else:
                pos[0] -= 1
        
        
        if pos == [0,0]:
            return True
        else:
            return False