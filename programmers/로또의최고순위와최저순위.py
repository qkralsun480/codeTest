def solution(lottos, win_nums):
    answer = []
    count =0
    zero_count = 0
    for data in lottos:
        if data in win_nums:
            count +=1
        elif data == 0:
            zero_count += 1
    max_count = count + zero_count
    answer.append(lottos_result(max_count))
    min_count = count
    answer.append(lottos_result(min_count))
    return answer

def lottos_result(count):
    if count == 6:
        return 1
    elif count == 5:
        return 2
    elif count ==4:
        return 3
    elif count == 3:
        return 4
    elif count == 2:
        return 5
    else:
        return 6
