# 프로그래머스 숫자 문자열과 영단어
def solution(s):
    num_dic = ['zero','one','two','three','four','five','six','seven','eight','nine']
    answer = 0
    if s.isalpha():
        return int(s)
    else:
        for i, v in enumerate(num_dic):
            s = s.replace(v,str(i))
    answer = int(s)
    return answer
