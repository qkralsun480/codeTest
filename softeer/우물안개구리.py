import sys

n,m = map(int, sys.stdin.readline().split())
w = list(map(int, sys.stdin.readline().split()))
weight_best = [True for _ in range(n)]
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    if w[a-1] > w[b-1]:
        weight_best[b-1] = False
    elif w[a-1] < w[b-1]:
        weight_best[a-1] = False
    else:
        weight_best[a-1] = False
        weight_best[b-1] = False
cnt =0
for answer in weight_best:
    if answer == True:
        cnt +=1

print(cnt)
