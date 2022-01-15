from collections import deque

def solution(board):
    dX = [1, -1, 0, 0]
    dY = [0, 0, 1, -1]
    queue = deque([])
    queue.append((0, 0, 0, 0))  # 좌표, 방향
    valueBoard = list([0] * len(board) for _ in range(len(board)))

    while queue:
        x, y, car_d, value = queue.popleft()
        for road_d in range(4):  # 동 서 남 북 방향
            nX = x + dX[road_d]
            nY = y + dY[road_d]

            if 0 <= nX < len(board) and 0 <= nY < len(board):
                if board[nY][nX] != 1:
                    if nX == 0 and nY == 0:
                        continue

    
                    if x == 0 and y == 0:
                        newValue = value + 100
                    else:
                        if car_d == road_d:
                            newValue = value + 100
                        else:
                            newValue = value + 600

                    if valueBoard[nY][nX] == 0:
                        valueBoard[nY][nX] = newValue
                        queue.append((nX, nY, road_d, newValue))
                    else:
                        if valueBoard[nY][nX] >= newValue:
                            valueBoard[nY][nX] = newValue
                            queue.append((nX, nY, road_d, newValue))


    return valueBoard[-1][-1]

board =[[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]

print(solution(board))
