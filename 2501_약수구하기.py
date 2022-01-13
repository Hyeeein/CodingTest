# 약수 구하기

while True:
    N, K = map(int, input().split())
    if 1 <= N <= 10000:
        break

K_list = []     # 약수 저장 리스트

for i in range(1, N+1):
    if N % i == 0:
        K_list.append(i)
    else:
        continue

if len(K_list) < K:
    print('0')
else:
    print(K_list[K-1])