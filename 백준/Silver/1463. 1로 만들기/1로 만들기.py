import sys

N = int(sys.stdin.readline())
dp = [0] * (N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    # dp[2] = dp[1]+1 = 0+1 = 1
    # dp[3] = dp[2]+1 = 1+1 = 2
    # dp[4] = dp[3]+1 = 2+1 = 3
    # dp[5] = dp[4]+1 = 2+1 = 3
    # dp[6] = dp[5]+1 = 3+1 = 4

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
        # dp[2] = min(dp[2], dp[1]+1) = 1
        # dp[4] = min(dp[4], dp[2]+1) = 2
        # dp[6] = min(dp[6], dp[3]+1) = 3

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
        # dp[3] = min(dp[3], dp[1]+1) = 1
        # dp[6] = min(dp[6], dp[2]+1) = 2

print(dp[N])