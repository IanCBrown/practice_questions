
# https://open.kattis.com/problems/acm

def main(): 
    total_score = 0 
    penalty = {} 
    correct_count = 0 
    
    while True:
        line = input().split()
        time = int(line[0]) 
        if time == -1:
            break
        problem = line[1]
        correctness = line[2]
        if correctness == "wrong":
            if problem in penalty:
                penalty[problem] += 20
            else:
                penalty[problem] = 20
        else:
            if problem not in penalty:
                total_score += time 
            else:
                total_score += time + penalty[problem]
            correct_count += 1
    
    print(str(correct_count) + " " + str(total_score))
        



if __name__ == "__main__": 
    main() 