def solution(s):
    answer = True

    # '('와 ')'의 개수가 맞지 않는 경우 / ')'로 시작
    open = 0
    for char in s:
        if char == '(':
            open += 1
        else:
            open -= 1
            if open < 0:
                answer = False
    
    if answer is not False and open == 0:
        ansewr = True
    else:
        answer = False
    
    return answer