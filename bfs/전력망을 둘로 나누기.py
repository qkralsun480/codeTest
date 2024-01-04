# 프로그래머스 전력망 둘로 나누기

from collections import deque
def solution(n, wires):
    answer = n
    graph= [[] for _ in range(n+1)]
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(start):
        cnt = 1
        visited= [0] * (n+1)
        q = deque([start])
        visited[start] =1
        while q:
            s = q.popleft()
            for k in graph[s]:
                if not visited[k]:
                    q.append(k)
                    visited[k] =1
                    cnt +=1
        return cnt
    for f,g in wires:
        graph[f].remove(g)
        graph[g].remove(f)
        
        answer = min(abs(bfs(f)-bfs(g)), answer)
        
        graph[f].append(g)
        graph[g].append(f)
    return answer
