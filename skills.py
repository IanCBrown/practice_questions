#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the differentTeams function below.
def differentTeams(skills):
    # each team can be considered as a set (no duplicates)
    # once a student is added to a set, remove them from the list

    teams = set()
    num_of_teams = 0 
    for i in range(len(skills)):
        teams.add(skills[i])
        if len(teams) == 5:
            num_of_teams += 1
            # clear teams 
            teams.clear()
        print(teams)
    return num_of_teams
        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    skills = input()

    res = differentTeams(skills)

    fptr.write(str(res) + '\n')

    fptr.close()
