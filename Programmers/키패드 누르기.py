# [2020 카카오 인턴십]
def find_dist(pos, target):
    x, y = pos[0], pos[1]
    tx, ty = target[0], target[1]
    return abs(x-tx) + abs(y-ty)

map = {
    1: (0,0),
    2: (0,1),
    3: (0,2),
    4: (1,0),
    5: (1,1),
    6: (1,2),
    7: (2,0),
    8: (2,1),
    9: (2,2),
    0: (3,1)
}

def solution(numbers, hand):
    answer = ''
    left_pos = (3,0)
    right_pos = (3,2)
    
    left_num = [1,4,7]
    right_num = [3,6,9]
    both_num = [2,5,8,0]
    
    for num in numbers:
        if num in left_num:
            left_pos = map[num]
            answer += 'L'
        
        if num in right_num:
            right_pos = map[num]
            answer += 'R'
            
        if num in both_num:
            target = map[num]
            left_dist = find_dist(left_pos, target = target)

            right_dist = find_dist(right_pos, target = target)

        
            if left_dist < right_dist:
                left_pos = map[num]
                answer += 'L'
            elif left_dist > right_dist:
                right_pos = map[num]
                answer +='R'

            else:
                if hand == 'right':
                    right_pos = map[num]
                    answer +='R'
                else:
                    left_pos = map[num]
                    answer +='L'
    
    return answer
