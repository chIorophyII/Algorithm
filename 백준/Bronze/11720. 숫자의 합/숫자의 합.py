import sys
N = int(sys.stdin.readline())
nums = sys.stdin.readline().rstrip()
answer = 0

for i in nums:
    answer += int(i)

print(answer)