from collections import deque

d = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def bfs(x,y):
    q = deque()
    q.append((x, y))
    graph[x][y] = '.'
    while q:
        dx ,dy = q.popleft()
        for a,b in d:
            X,Y = dx+a, dy+b
            if (0 <= X < x_len) and (0 <= Y < y_len) and graph[X][Y] == '#':
                q.append((X,Y))
                graph[X][Y] = '.'
                
for _ in range(int(input())):
    x_len, y_len = map(int,input().split())
    graph = [list(input()) for _ in range(x_len)]
    count =0
    for i in range(x_len):
        for j in range(y_len):
            if graph[i][j] == '#':
               bfs(i,j)
               count +=1
print(count)
