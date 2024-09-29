def solution(citations):
    answer = 0
    
    # 정렬하면 0, 1, 3, 5, 6
    citations.sort()
    n = len(citations)  # 길이는 5
    
    # 부터 0까지 -1씩 감소하는 반복문
    for i in range(n):
        h_index = n-i  # 가장 큰 h를 구하는 것이므로 가장 큰 것부터 구해봄 (5 빼기 0은 5)
        
        # 정렬했던 citations의 인덱스 앞부터 h_index와 비교
        # h_index보다 citations 원소 값이 같거나 커지는 순간 종료
        if citations[i] >= h_index:
            answer = h_index
            break
    return answer