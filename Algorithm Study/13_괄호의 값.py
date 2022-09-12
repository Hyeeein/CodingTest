# 괄호열을 나타내는 문자열 입력 (1 이상, 30이하)
while True:
    str = list(input())
    if 1<= len(str) <= 30:
        break

# 전역변수
n = len(str)  # 문자열의 길이
stack = []  # 스택 초기화
result = 0
tmp = 1  # 조건 1, 2 계산을 위해 생성

# 괄호의 값 계산 : 왼쪽 괄호 만날 땐 계속 스택 안에 삽입하다가 오른쪽 괄호 나오면 짝이 맞는지 검사 후 계산
for i in range(n):

    # 왼쪽 괄호일 경우
    if str[i] == '(':
        tmp *= 2
        stack.append(str[i])

    elif str[i] == '[':
        tmp *= 3
        stack.append(str[i])
    
    # 오른쪽 괄호일 경우
    elif str[i] == ')':
        if not stack or stack[-1] == '[': # 스택이 비었거나 마지막 요소 괄호가 맞지 않을 경우
            result = 0
            break
        if str[i-1] == '(': # 마지막 요소 괄호가 맞을 경우 (이전 요소와 다음 요소가 ())
            result += tmp
        tmp = tmp // 2
        stack.pop() # 계산했으니까 리스트에서 뺌

    elif str[i] == ']':
        if not stack or stack[-1] == '(':
            result = 0
            break
        if str[i-1] == '[': # 이전 요소와 다음 요소가 []
            result += tmp
        tmp = tmp // 3
        stack.pop()

if stack:
    print(0)
else:
    print(result)


# --- 함수 --- # 때려치움...
# def push(data):
#     global n, stack, top
#     if (top >= n - 1):
#         print('스택 꽉 참')
#         return
#     top += 1
#     stack[top] = data

# def pop(data):
#     global n, stack, top
#     if (top == -1):
#         print('스택 빔')
#     data = stack[top]
#     stack[top] = None
#     top -= 1
#     return data
