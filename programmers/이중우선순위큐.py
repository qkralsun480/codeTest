# 프로래머스 이중우선순위 큐
import heapq

def solution(operations):
    answer = []
    heap = []

    for data in operations:
        # heap에 추가 heap = [-5,7,5]
        if data[0] == "I":
            heapq.heappush(heap, int(data[2:]))
        # 연산이 "D"일 경우
        else:
            if len(heap) == 0:
                pass
            # 공백 뒤가 "-"일 경우 최소힙을 제거
            elif data[2] == "-":
                heapq.heappop(heap)
            # 공백 뒤가 아무것도 아닌 경우
            else:
                # 힙에서 가장 큰 수를 제외하고 다시 힙에 넣음
                # 함수를 사용하면 list에서 가장 큰 n개의 수를 뽑아낼 수 있다.
                # 리스트 x를 즉각적으로 heap으로 변환함 : heapify
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)

    if heap:
        answer.append(max(heap))
        answer.append(min(heap))
    else:
        answer.append(0)
        answer.append(0)
    
    return answer
