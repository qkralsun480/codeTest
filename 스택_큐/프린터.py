from collections import deque

def solution(priorities, location):
    answer = 0
    from collections import deque

    d = deque([(v,i) for i,v in enumerate(priorities)])

    while len(d):
        item = d.popleft()
        # value중에서 최댓값을 찾아야하기 때문이다. max(d)[0] 0인덱시 붙이는 이유
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer
