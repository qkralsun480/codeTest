
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
    
# 시간초과 
# import sys
# input = sys.stdin.readline

# n,x = map(int, input().split())
# data = list(map(int, input().split()))

# sum_data = []
# period_list = []
# for i in range(0,len(data)-x+1):  
#     sum_d =0
#     for j in range(i,i+x):
#         sum_d += data[j]
#     sum_data.append(sum_d)

# answer_value = max(sum_data)
# answer_count = sum_data.count(answer_value)
# if answer_value == 0:
#     print('SAD')
# else:
#     print(answer_value)
#     print(answer_count)
