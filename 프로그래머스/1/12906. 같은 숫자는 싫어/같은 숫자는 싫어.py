def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        # 첫 번째 원소
        if i == 0:
            answer.append(arr[i])   
        
        # 두 번째 이후 원소
        else:
            if arr[i-1] == arr[i]:
                continue
            else:
                answer.append(arr[i])
        
    return answer