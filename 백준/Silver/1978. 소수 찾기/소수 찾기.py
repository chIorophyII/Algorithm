import sys
N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
answer = 0

for i in nums:
    if i == 1:
      continue
    half = i//2
    for j in range(half, 0, -1):
        if j == 1:
            answer += 1
            break
        if i % j == 0:
            break

print(answer)