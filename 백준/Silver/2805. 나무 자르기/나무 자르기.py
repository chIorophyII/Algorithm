import sys

N, M = map(int, sys.stdin.readline().split())
tree_list = list(map(int, sys.stdin.readline().split()))
left = 0
right = max(tree_list)
length = 0

while left <= right:
    # 11 <= 20
    # 11 <= 15
    mid = (left + right) // 2
    # 0+20 // 2 = 10
    # 11+20 // 2 = 16
    hap = 0
    for tree in tree_list:
        if tree > mid:
            # 20 > 10
            # 20 > 16, 17 > 16
            hap += tree - mid
            # hap += 20-10 = 10
            # hap += 20-16 = 4 += 17 - 16 = 1 == 5
        if hap >= M: # 10 > 7
            break

    if hap >= M:
        # 10 > 7
        length = max(length, mid)
        # max(0, 10) = 10
        left = mid + 1 # left = 11
    else:
        right = mid -1
        # right = 16-1 = 15


print(length)