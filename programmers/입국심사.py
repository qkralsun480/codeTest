# 이분탐색문제: 이분 탐색은 탐색 기법 중 하나로써 원하는 탐색 범위를 두 부분으로 분할해서 찾는 방식
# 탐색 범위의 처음(left)과 끝(right)의 중간(mid)과 탐색하고자 하는 값을 비교
# 탐색 값이 중간(mid)보다 작은 경우에는 범위의 끝(right)을 중간-1(mid -1)값 설정
# 탐색 값이 중간(mid)보다 큰 경우에는 범위의 처음(left)을 중간+1(mid+1)값으로 설정한다.
# 점수 : 985

def solution(n, times):
    answer = 0
    left = min(times)
    right = max(times) * n
    while left <= right:
        mid = (left + right) // 2
        checked = 0
        for time in times:
            checked += mid // time
            if checked >= n:
                break
        if checked >=n:
            answer = mid
            right = mid-1
        elif checked < n:
            left = mid +1
            
    return answer
