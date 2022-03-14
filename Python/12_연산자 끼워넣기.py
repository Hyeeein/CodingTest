# 첫째 줄에 N 입력받기 (2이상 11이하)
N = int(input())

# 둘째 줄에 N개만큼 숫자 입력
N_num = list(map(int, input().split(' ')))

# 셋째 줄에 합이 N-1인 4개의 정수 (차례대로 덧셈, 뺄셈, 곱셈, 나눗셈의 개수)
while True:
    add, sub, mul, div = map(int, input().split(' '))
    if (add + sub + mul + div) == N-1:
        break

# 연산자 조합해서 계산 (재귀함수 사용)
max_num, min_num = -1000000001, 1000000001

# 횟수, 0번째 인덱스 값, + 개수, - 개수, * 개수, / 개수
def calculate(count, result, add, sub, mul, div):
    global max_num, min_num

    # N번 하고나면 종료
    if count == N:
        max_num = max(max_num, result)
        min_num = min(min_num, result)
        return
    
    # 각 연산자 갯수가 남아있을 때 실행 (연산자 우선순위 무시)
    if add > 0:
        calculate(count + 1, result + N_num[count], add-1, sub, mul, div)
    if sub > 0:
        calculate(count + 1, result - N_num[count], add, sub-1, mul, div)
    if mul > 0:
        calculate(count + 1, result * N_num[count], add, sub, mul-1, div)
    if div > 0:
        # 음수를 양수로 나눌 때 양수로 바꾸고 몫 구하고 다시 음수로 바꿈
        if result < 0:
            calculate(count + 1, -(-result // N_num[count]), add, sub, mul, div-1)
        else:
            calculate(count + 1, result // N_num[count], add, sub, mul, div-1)
#-----------------------------------------
# count 값은 1부터 시작, N_num[0]부터 
calculate(1, N_num[0], add, sub, mul, div)
print(max_num)
print(min_num)


# 명시적 제약 조건 : 트리의 각 노드는 0 또는 1의 값을 가진다. 
# 이때 i번째 높이의 노드는 i번째 원소의 선택 여부를 나타내며 
# 0은 선택하지 않음, 1은 선택함을 나타낸다.

# 출처: https://it00.tistory.com/26 [IT
