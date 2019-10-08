import sys


info_line = sys.stdin.readline().split()
num_socks = int(info_line[0])
capicity = int(info_line[1])
max_color_diff = int(info_line[2])

data_line = sys.stdin.readline().split()

socks = []

for sock in data_line:
    socks.append(int(sock))
socks.sort()

machines_needed = 1
sock_counter = 1 
min_sock = socks[0]

for i in range(1, num_socks):
    if sock_counter == capicity:
        machines_needed += 1
        sock_counter = 0
        min_sock = socks[i]
    if socks[i] - min_sock > max_color_diff:
        machines_needed += 1
        sock_counter = 0
        min_sock = socks[i]
    sock_counter += 1
print(machines_needed)