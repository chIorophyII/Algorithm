import sys
N = int(sys.stdin.readline())
maxi = -1000000
mini = 1000000

for i in map(int, sys.stdin.readline().split()):
    if i > maxi:
        maxi = i
    if i < mini:
        mini = i

print("{0} {1}".format(mini, maxi))