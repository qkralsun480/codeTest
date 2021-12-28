import sys
from collections import deque

dx= [0,0,-1,1]
dy= [1,-1,0,0]

n,m =map(int, sys.stdin.readline().split())
field = []

for _ in range(m):
    field.append(list(map(int, sys.stdin.readline().split(" "))))
    
def bfs():
    de =deque()
    de.append((0,0))
    count =0
    visited = [[False] * m for i in range(n)]
    
    while de:
        x,y = de.popleft()
        for i in range(4):
            nx =  x + dx[i]
            ny =  y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:
            if field[nx][ny] == 0 and visited[nx][ny] == False:
                visited[nx][ny] = True
                de.append((nx,ny))
        elif field[nx][ny] == 1:
            field[nx][ny] = 0
            count += 1
            visited[nx][ny] = True
    return count
            
result = []
time =0
while True:
    count = bfs()
    result.append(count)
    if count ==0:
        break
    time +=1

print(time)
print(result[-2])
