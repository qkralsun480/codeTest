def solution(gems):
    size = len(set(gems))
    # gems 의 종류 ( 중복되지 않는 원소의 값을 리턴)
    dic = {gems[0]:1}
    print(dic)
    temp = [0, len(gems) - 1]
    start , end = 0, 0

    while(start < len(gems) and end < len(gems)):
        if len(dic) == size:
            if end - start < temp[1] - temp[0]:
                temp = [start, end]
            if dic[gems[start]] == 1:
                del dic[gems[start]]
                print(dic)
            else:
                dic[gems[start]] -= 1
                print(dic)
            start += 1

        else:
            end += 1
            if end == len(gems):
                break
            if gems[end] in dic.keys():
                dic[gems[end]] += 1
                print(dic)
            else:
                dic[gems[end]] = 1
                print(dic)

    return [temp[0]+1, temp[1]+1]

gems =["AA", "AB", "AC", "AA", "AA","AB","AC"]
print(solution(gems))

'''
["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	[3, 7]
["AA", "AB", "AC", "AA", "AA","AB","AC"]	[1, 3]
["XYZ", "XYZ", "XYZ"]	[1, 1]
["ZZZ", "YYY", "NNNN", "YYY", "BBB"] [1, 5]
'''
