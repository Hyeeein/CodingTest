def solution(progresses, speeds):
    answer = []
    day_list = []
    
    # 걸리는 시간
    for i in range(len(progresses)):
        day = 0
        while progresses[i] < 100:
            if progresses[i] >= 100:
                break
            
            progresses[i] += speeds[i]
            day += 1
        day_list.append(day)
    
    # 배포 날
    index_list = [] # 이미 배포된 것들
    count = 0       # 같은 날 배포된 것들
    
    for j in range(len(day_list)):
        if j not in index_list:
            now = day_list[j]
            index_list.append(j)
            count += 1

            for k in range(j+1, len(day_list)):
                if day_list[k] <= now:
                    count += 1
                    index_list.append(k)
                else:
                    break
            answer.append(count)
            count = 0
        
    return answer