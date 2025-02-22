def solution(answers):
    answer = []
     
    # 수포자 답안
    person_1 = [1, 2, 3, 4, 5]
    person_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 맞은 개수 count
    one_count = 0 ; two_count = 0 ; three_count = 0
    
    # 수포자 답안을 answers 개수만큼 만들기 (문제보다 짧은 경우만)
    answers_len = len(answers)
    num_1, num_2, num_3 = 0, 0, 0
    
    if len(person_1) < answers_len:
        num_1 = person_1 * ((answers_len // len(person_1)) + (answers_len % len(person_1)))
    else:
        num_1 = person_1[:answers_len]
    
    if len(person_2) < answers_len:
        num_2 = person_2 * ((answers_len // len(person_2)) + (answers_len % len(person_2)))
    else:
        num_2 = person_2[:answers_len]
    
    if len(person_3) < answers_len:
        num_3 = person_3 * ((answers_len // len(person_3)) + (answers_len % len(person_3)))
    else:
        num_3 = person_3[:answers_len]
    
    for i in range(answers_len):
        if num_1[i] == answers[i]: one_count += 1
        if num_2[i] == answers[i]: two_count += 1
        if num_3[i] == answers[i]: three_count += 1
    
    max_count = max(one_count, two_count, three_count)
    if one_count == max_count: answer.append(1)
    if two_count == max_count: answer.append(2)
    if three_count == max_count: answer.append(3)
    
    return answer