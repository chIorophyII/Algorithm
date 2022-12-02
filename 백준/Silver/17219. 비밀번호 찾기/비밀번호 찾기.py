import sys
N, M = map(int, sys.stdin.readline().split())

dic = dict()
for i in range(N):
    site, pw = sys.stdin.readline().split()
    dic[site] = pw

for i in range(M):
    site = sys.stdin.readline().rstrip()
    print(dic[site])