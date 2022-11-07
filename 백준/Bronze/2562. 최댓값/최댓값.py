import sys
maxi = 0
maxi_idx = 0

for i in range(9):
    N = int(sys.stdin.readline())
    if N > maxi:
        maxi = N
        maxi_idx = i+1

print(maxi)
print(maxi_idx)