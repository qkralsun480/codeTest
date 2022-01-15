import re
from itertools import permutations

def solution(expression):
    #1
    op = [x for x in ['*','+','-'] if x in expression]
    print(op)
    op = [list(y) for y in permutations(op)]
    print(op)
    ex = re.split(r'(\D)',expression)
    #정규식 \D 숫자가 아닌 문자열로 인식할수 있는 정규식
    # ['100', '-', '200', '*', '300', '-', '500', '+', '20']
    #2
    a = []
    for x in op:
        result_list= ex[:]
        for y in x:
            while y in result_list:
                tmp = result_list.index(y)
                print(tmp)
                # 해당 수식이  있는 곳의 인덱스를 반환
                result_list[tmp-1] = str(eval(result_list[tmp-1]+result_list[tmp]+result_list[tmp+1]))
                #_ex = _ex[:tmp]+_ex[tmp+2:]
                del result_list[tmp:tmp+2]
        a.append(result_list[0])

    #3
    return max(abs(int(x)) for x in a)

expression ="100-200*300-500+20"
print(solution(expression))
