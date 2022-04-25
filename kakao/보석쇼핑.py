# 투포인터를 이용한 문제풀이
def solution(gems):
    size = len(set(gems))
    start = 0 
    end = len(gems) - 1 
    s = set() 
    for i in range(len(gems)):
        for j in range(i, len(gems)):
            s.add(gems[j]) 
            if len(s) == size and end - start > j - i:
                start = i 
                end = j 
                break
        s.clear()
    return [start + 1, end + 1]

gems =["AA", "AB", "AC", "AA", "AA","AB","AC"]
print(solution(gems))

'''
["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	[3, 7]
["AA", "AB", "AC", "AA", "AA","AB","AC"]	[1, 3]
["XYZ", "XYZ", "XYZ"]	[1, 1]
["ZZZ", "YYY", "NNNN", "YYY", "BBB"] [1, 5]
'''
