class Solution:
    def getHint(self, secret, guess):
        secret_info = [0] * 10    
        guess_info = [0] * 10
        
        bulls = 0 
        cows = 0 
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bulls += 1
            else:
                secret_info[int(secret[i])] += 1
                guess_info[int(guess[i])] += 1
                
        for i in range(10):
            cows += min(secret_info[i], guess_info[i])

                
        return str(bulls) + "A" + str(cows) + "B"

