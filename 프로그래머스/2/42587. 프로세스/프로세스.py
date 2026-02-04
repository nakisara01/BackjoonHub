def solution(priorities, location):
    answer = 0
    
    while True:
        now = priorities.pop(0)
        
        if priorities and max(priorities) > now:
            priorities.append(now)
            if location == 0:
                location += len(priorities) - 1
            else:
                location -= 1
        else:
            answer += 1
            if location > 0:
                location -= 1
            else:
                return answer