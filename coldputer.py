# input: First line, number of temps recorded, Second line, the actual temperatures
# output: the number of temperatures below zero 
import sys

num_of_temps = int(input())

# for i in range(num_of_temps):
for i in sys.stdin:
    temps_list = i.split()

counter = 0 
for i in temps_list:
    if int(i) < 0:
        counter = counter + 1

print(counter)

