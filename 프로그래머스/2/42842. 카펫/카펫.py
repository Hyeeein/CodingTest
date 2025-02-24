def solution(brown, yellow):
    answer = []
    total_carpets = brown + yellow
    
    # 약수 구하기 (1과 자기 자신 제외)
    number_list_yellow = [i for i in range(1, yellow + 1) if yellow % i == 0]
    
    # 조합을 찾아보자 (완전 탐색!)
    results_yellow = []
    for i in number_list_yellow:
        for j in number_list_yellow:
            if i * j == yellow and i >= j: # i >= j는 가로 길이가 세로보다 긴 것
                results_yellow.append([i, j])
    # print(results_yellow)
    
    # 찾은 조합 중에서 중앙은 노란색, 테두리 1줄은 갈색인 것
    for i, j in results_yellow:
        if (i+2) * (j+2) == total_carpets:
            answer.append(i+2)
            answer.append(j+2)
    
    return answer