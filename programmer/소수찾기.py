from itertools import permutations
import math

def solution(numbers):
    number_list = list(numbers)
    answer = 0
    temp = []
    for c in range(1,len(number_list)+1):
        temp.extend(sorted(list(set(map(''.join, permutations(number_list, c))))))
    result_list = list(set(map(int, temp)))
    for data in result_list:
         if prime_check(data):
             answer += 1
    return answer

def prime_check(n):
    n = int(n)
    if n == 1 or n == 0:
        return False
    for div in range(2,int(math.sqrt(n))+1):
        if n%div == 0:
            return False
    if True:
        print(n)
    return True

def main():
    numbers = "011"
    result = solution(numbers)
    print(result)

if __name__ == "__main__":
	main()
'''
numbers	return
"17"	3
"011"	2
'''

''''
#|는 or 연산자이고 union을 뜻한다.그래서 |= 는 |의 결과를 update한다는 뜻이다..
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
'''

'''
소수의 판별 : 기본적인 알고리즘 성능분석
2부터 x-1까지의 모든 자연수에 대해여 연산을 수행해야 합니다.
- 모든 수를 하나씩 확인한다는 점에서 시간 복잡도 O(X) 입니다.

2부터 x의 제곱근까지의 모든 자여수에 대하여 연산을 수행하면
시간 복잡도는 O(n2/1)
'''
