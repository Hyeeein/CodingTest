def solution(number, k):
    answer = ''
    
    # 숫자 리스트로 변환
    number_ = list(number) # ['1', '9', '2', '4']
    number_list = [int(i) for i in number_] # [1, 9, 2, 4]
    
    # 스택 활용
    stack = []
    for num in number_list:
        # 스택이 비어 있지 않고, 스택의 마지막 값이 num보다 작으며, k가 0보다 클 때
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    
    # k가 0이 아닌 경우 맨 마지막 숫자부터 삭제
    if k != 0:
        stack = stack[:-k]
    
    stack_ = [str(i) for i in stack]
    answer = ''.join(stack_)
    
    return answer