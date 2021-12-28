import sys

input = sys.stdin.readline

for _ in range(int(input())):
    # 문자열을 아스키코드로
    v = list(map(lambda x: ord(x) - 97, input().strip()))
    k, min_len, max_len = int(input()), len(v), -1


    pos = [[] for _ in range(26)]
    for idx, val in enumerate(v): # key, value
        pos[val].append(idx)
    no_exist = True
    
    print(pos)
    # k칸 떨어진 알파벳 사이 거리는 list에서 k칸 떨어진 인덱스들을 슬라이딩 윈도우로 한 칸씩 밀면서 갱신
    for p in pos:
        if len(p) >= k:
            no_exist = False
            for i in range(len(p) - k + 1):
                min_len = min(min_len, p[i + k - 1] - p[i] + 1) 
                max_len = max(max_len, p[i + k - 1] - p[i] + 1)

    if no_exist:
        print(-1)
    else:
        print(min_len + 1, max_len + 1)
        
# superaquatornado
