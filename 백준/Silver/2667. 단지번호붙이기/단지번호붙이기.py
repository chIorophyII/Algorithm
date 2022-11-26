import sys
from collections import deque

N = int(sys.stdin.readline())

# 행렬 만들기
graph = [list(map(int, input())) for _ in range(N)]

def bfs(graph, x, y):
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque() # 하나의 단지 그룹이 들어갈 queue
    queue.append((x, y))
    graph[x][y] = 0  # 탐색중인 위치 0으로 바꿔 다시 방문하지 않도록 함
    cnt = 1

    while queue: # 하나의 단지에 대해서 탐색
        x, y = queue.popleft()

        for i in range(4): # 상하좌우를 살핌
            nx = x + dx[i]
            ny = y + dy[i]

            # 벗어난 범위
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if graph[nx][ny] == 1: # 탐색안된 위치에 대해
                graph[nx][ny] = 0 # 탐색 표시
                queue.append((nx, ny))
                cnt += 1
    return cnt


count = [bfs(graph, i, j) for i in range(N) for j in range(N) if graph[i][j] == 1]

count.sort()
print(len(count))

for i in range(len(count)):
    print(count[i])