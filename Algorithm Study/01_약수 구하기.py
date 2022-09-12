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

## k_list = [i for i in range(1, N+1) if N % i == 0]

## 정윤님 답안
# try:
#     n, k = map(int, input('숫자를 입력해 주세요').split())
#     if not (1 <= n <= 10000 and 1 <= k <= n): # 예외 범위 정하기
#         raise Exception('잘못 입력하셨습니다.')
#     # a=[i for i in range(1, A+1) if A%i == 0]
#     a = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             a.append(i)
#
#     print(a[k - 1])
# except IndexError:
#     print(0)
# except Exception as e:
#     print(e)
