def solution(land):
    answer = 0
    for i in range(1,len(land)):
        #dp를 활용 4열까지 있어서 열별로 체크
        #이전값을 저장해야되는경우는 .....dp....(?)
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
        land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])
    return max(land[-1])
