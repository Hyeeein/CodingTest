from collections import deque

def solution(progresses, speeds):    
    # 걸리는 시간
    day_list = []
    
    for i in range(len(progresses)):
        day = 0
        while progresses[i] < 100:
            if progresses[i] >= 100:
                break
            
            progresses[i] += speeds[i]
            day += 1
        day_list.append(day)
    
    # 배포 날
    answer = []
    queue = deque(day_list)
    
    while queue:
        count = 1
        first = queue.popleft() # 첫 번째 배포 가능 날짜
        
        # 배포될 기능 추가 count
        while queue:
            if queue[0] <= first:
                queue.popleft()
                count += 1
            else:
                break
        
        answer.append(count)
        
    return answer