## 레벨2 : 968점
def solution(record):
    answer = []
    result_data = {}
    for i in record:
        split_record = i.split()
        if split_record[0] != 'Leave':
            result_data[split_record[1]] = split_record[2]   
    
    for j in record:
        split_record_2 = j.split()
        if split_record_2[0] == 'Enter':
            answer.append(result_data[split_record_2[1]]+'님이 들어왔습니다.')
        elif split_record_2[0] == 'Leave':
            answer.append(result_data[split_record_2[1]]+'님이 나갔습니다.')
     
    return answer
