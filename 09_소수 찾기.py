# 소수 : 약수가 본인과 1만 가지는 수

N = int(input())                     # 수의 개수 : 100 이하
N_num = list(map(int, input().split(' '))) # 1000 이하의 자연수

PN_count = 0    # 주어진 수들 중 소수의 개수
for i in range(N):
    N_count = 0  # 각 숫자별 소수의 개수 (초기화)

    for j in range(1, N_num[i] + 1):
        if N_num[i] % j == 0:
            N_count += 1
    
    if N_count == 2:  # 1과 본인
        PN_count += 1

print(PN_count)
