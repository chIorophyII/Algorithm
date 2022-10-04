import sys
In = sys.stdin.readline
N, K = map(int, In().strip().split())
cnt = 0
answer = 0

for i in range(1, N+1):
    if N % i == 0:
        cnt += 1
        if cnt == K:
            answer = i
            break

print(answer)