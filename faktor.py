# input: two numbers: number of articles to publish, desired impact factor
# output: minimum number of scientist needed to be bribed 
# cc: if min num of scientest / num of articles == desired impact factor 
import sys, math 

for i in sys.stdin:
    ab = i.split()
    num_articles = int(ab[0])
    impact_desired = int(ab[1])

num_scientist = num_articles * impact_desired

impact_desired_possible = True

while impact_desired_possible == True:
    if math.ceil(num_scientist / num_articles) == impact_desired:
        num_scientist = num_scientist - 1
    else:
        impact_desired_possible = False

# adding one is a cheap solution!
print(str(num_scientist + 1))
