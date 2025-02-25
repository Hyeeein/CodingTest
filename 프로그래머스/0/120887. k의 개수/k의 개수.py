def solution(i, j, k):
    answer = 0
    
    for num in range(i, j+1):
        num_str = str(num)
        k_str = str(k)
        
        for n in num_str:
            if k_str == n: answer += 1
    
    return answer