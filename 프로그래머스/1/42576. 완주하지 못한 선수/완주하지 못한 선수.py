def solution(participant, completion):
    answer = ''
    
    # 효율성 테스트로 인해 sort 후 진행
    participant.sort()
    completion.sort()
    
    for i in range(len(participant)-1): # completion이 값이 하나 적으니까
        if participant[i] != completion[i]:
            answer = participant[i]
            return answer
        
    answer = participant[-1]
        
    return answer