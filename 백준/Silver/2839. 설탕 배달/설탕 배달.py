import sys

N = int(sys.stdin.readline())
result = 0

while N >= 0:

    if N % 5 == 0:
        result += N // 5
        break

    N -= 3
    result += 1

else:
    result = -1

print(result)