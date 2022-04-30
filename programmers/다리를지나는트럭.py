## 아이디어
## bridge_length 에 최대로 올라 갈 수 있는 트럭의 무게 구하기
## 다리를 지나는 트럭(기존) weight + 새로 지나는 트럭의 무게 < wight 일경우에만 trucks_on_bridge에 추가
## 아닐 경우에는 0 을 추가
def solution(bidge_length, weight, truck_weights):
    answer = 0
    trucks_on_bridge = [0] * bridge_length
    while len(trucks_on_bridge):
        answer += 1
        trucks_on_bridge.pop(0)
        if truck_weights:
            if sum(trucks_on_bridge) + truck_weights[0] <= weight:
                trucks_on_bridge.append(truck_weights.pop(0))
            else:
                trucks_on_bridge.append(0)
    return answer
