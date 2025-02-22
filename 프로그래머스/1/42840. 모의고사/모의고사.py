def solution(answers):
    answer = []
     
    # 수포자 답안 패턴
    person_1 = [1, 2, 3, 4, 5]
    person_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 맞은 개수 count
    one_count = 0 ; two_count = 0 ; three_count = 0
    
    # 정답 개수
    answers_len = len(answers)
    
    num_1 = person_1 * ((answers_len // len(person_1)) + (answers_len % len(person_1)))
    num_2 = person_2 * ((answers_len // len(person_2)) + (answers_len % len(person_2)))
    num_3 = person_3 * ((answers_len // len(person_3)) + (answers_len % len(person_3)))
    
    # 정답 비교
    for i in range(answers_len):
        if num_1[i] == answers[i]: one_count += 1
        if num_2[i] == answers[i]: two_count += 1
        if num_3[i] == answers[i]: three_count += 1
    
    # 가장 많이 맞힌 사람 찾기
    max_count = max(one_count, two_count, three_count)
    if one_count == max_count: answer.append(1)
    if two_count == max_count: answer.append(2)
    if three_count == max_count: answer.append(3)
    
    return answer