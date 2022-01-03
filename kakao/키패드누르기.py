def solution(numbers, hand):
    answer = ''
    left_distance = 0
    right_distance = 0
    left_hand_location = '*'
    right_hand_location = '#'
    
     # 번호 좌표화
    number_position = {1:(0, 0), 2:(0, 1), 3:(0, 2),
                4:(1, 0), 5:(1, 1), 6:(1, 2),
                7:(2, 0), 8:(2, 1), 9:(2, 2),
                '*':(3, 0), 0:(3, 1), '#':(3, 2)}
    
    for number in numbers:
        if number in (1,4,7):
            answer += 'L'
            left_hand_location = number
        elif number in (3,6,9):
            answer += 'R'
            right_hand_location = number
        elif number in (2, 5, 8, 0):
            # 거리계산 abs절대값
            left_distance = abs(number_position[left_hand_location][0]-number_position[number][0]) + abs(number_position[left_hand_location][1]-number_position[number][1] )
            right_distance = abs(number_position[right_hand_location][0]-number_position[number][0]) + abs(number_position[right_hand_location][1]-number_position[number][1] )
            if left_distance > right_distance:
                answer += 'R'
                right_hand_location = number
            elif left_distance < right_distance:
                answer += 'L'
                left_hand_location = number
            # 거리가 같을경우
            elif left_distance == right_distance:
                if hand == 'right':
                    answer += 'R'
                    right_hand_location = number
                elif hand == 'left':
                    answer += 'L'
                    left_hand_location = number
    return answer 
