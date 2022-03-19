
import sys
input = sys.stdin.readline

# n,x = map(int, input().split())
# data = list(map(int, input().split()))
n,x = 5, 2
data = [1, 4, 2, 5, 1 ] 
# 0 1 5 7 12 13
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

result = []

cnt = 0  
while cnt+x <= n:
    result.append(prefix_sum[cnt+x]-prefix_sum[cnt])
    cnt += 1
    
    
if max(result) == 0:
    print('SAD')
else:
    print(max(result))
    print(result.count(max(result)))
