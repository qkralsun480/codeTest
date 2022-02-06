from collections import deque

def bfs(arr_list):
    people_location = []
    for i in range(5):
        for j in range(5):
            if arr_list[i][j] == 'P':
                people_location.append([i,j])
    print(people_location)
    
    for data in people_location:
        queue = deque([data])
        visited = [[0]*5 for i in range(5)]   # 방문 처리 리스트
        print(visited)
        distance = [[0]*5 for i in range(5)]  # 경로 길이 리스트
        visited[data[0]][data[1]] = 1
        
        while queue:
            x,y = queue.popleft() 

            dx = [1,-1,0,0]
            dy = [0,0,-1,1]
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                ## 이부분을 생각해야 할듯
                if 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == 0:
                    if arr_list[nx][ny] == 'O':
                        queue.append([nx][ny])
                        visited[nx][ny] = 1
                        distance[nx][ny] = distance[x][y]+1
                    if arr_list[nx][ny] == 'P' and distance[x][y]<=1:
                        return 0
    return 1
                          
                      
                        
    
def solution(places):
    answer = []
    
    for i in places:
        answer.append(bfs(i))  
    return answer

def main():
    places = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
    ]
    result = solution(places)
    print(result)

if __name__ == "__main__":
	main()
'''
[1, 0, 1, 1, 1'
'''
