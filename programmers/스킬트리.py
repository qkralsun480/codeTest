# 프로그래머스 스킬트리
def solution(skill, skill_trees):
    answer = 0

    for data in skill_trees :
        skillTmp = skill
        flag = True
        for i in range(len(data)):
            if data[i] in skillTmp:
                # 첫번째 행을 검사
                if data[i] == skillTmp[0]:
                    skillTmp = skillTmp[1:]
                else :
                    flag = False
        if flag :
            answer += 1


    return answer
