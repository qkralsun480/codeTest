import sys
from collections import deque
N = int(sys.stdin.readline())
blockMap = [list(map(int, input())) for _ in range(N)]
visitedMap = [[False]* N for _ in range(N)]

def dfs(x,y):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    q = deque()
    visitedMap[x][y] = True
    q.append([x,y])
    cnt = 1
    while q:
        r, c = q.popleft()
        for k in range(4):
            dx_x = dx[k] + r
            dy_y = dy[k] + c
            if (0<=dx_x < N and 0<=dy_y < N) and blockMap[dx_x][dy_y] ==1 and not visitedMap[dx_x][dy_y]:
                visitedMap[dx_x][dy_y] = True
                # 큐에 추가하기
                cnt +=1
                q.append([dx_x,dy_y])
    return cnt
result = []
for i in range(N):
    for j in range(N):
        if blockMap[i][j] ==1 and not visitedMap[i][j]:
            result.append(dfs(i,j))
            
print(len(result))
result.sort()
for ans in result:
    print(ans)
