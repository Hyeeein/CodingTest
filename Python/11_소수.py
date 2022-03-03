# 두 개의 수를 입력받음
a = int(input())
b = int(input())

N_sum = 0   # 소수의 합
N_min = []   # 소수 리스트

for i in range(a, b+1, 1):
    N_count = 0 # 각 숫자별 약수의 개수 (초기화)

    for j in range(1, i+1):
        if i % j == 0:
            N_count += 1
    
    if N_count == 2:    # 소수일 경우 더하기
        N_sum += i
        N_min.append(i)

# 소수가 있을 경우, 합과 최소값 출력
if N_sum > 0:
    print(N_sum)
    print(N_min[0])
# 소수가 없을 경우 -1 출력
else:
    print(-1)






# ### ------------------------
# ### 재영님
# # 1. 자연수 M 과 N
# M = int(input("10,000 이하의 자연수 1을 입력하시오: "))
# N = int(input("10,000 이하의 자연수 1을 입력하시오: "))

# # 2. M과 N 사이의 숫자들 (즉, N은 M보다 크거나 같아야 하고, 10,000보다 작아야 한다!)
# if M > N:
#     print("M은 N보다 작거나 같아야 합니다!")
# elif M > 10000 or N > 10000:
#     print("M과 N은 모두 10,000 이하의 자연수여야 합니다!")

# # 3. 소수(prime number) 구하기
# else:
#     PM = []
#     for i in range(M, N+1):
#         result = True
#         if i < 2:
#             result = False
#         for j in range(2, i):
#             if(i%j == 0):
#                 result = False
#         if result:
#             PM.append(i)

# if len(PM) == 0:
#     print(-1)
# else:
#     print(PM)

# # 4. 구한 소수들의 합 구하기
#     S = sum(PM)
#     print(S)

# # 5. 구한 소수들의 최소값 구하기
#     m = PM[0]
#     print(m)

# '''
# * 소수를 구하는 예시들 중 하나
# n = 1000                           # 숫자의 갯수 n
# for i in range(n+1):               # 해당 숫자까지의 모든 자연수들 i
#     result = True                  # 초기 상태는 모두 진실
#     if i < 2:                      # 2보다 작은 자연수들 (1)
#         result = False             # 소수가 아니므로 거짓
#     for j in range(2, i):          # 2부터 해당 숫자까지의 모든 자연수들 j
#         if(i%j == 0):              # i를 j로 나누었을 때 나머지가 없을 때, 즉 배수일 경우
#             result = False         # 소수가 아니므로 거짓
#     if result:
#         print(i, end=" ")
# '''


# ### ------------------
# ## 정윤님
# # 백준 2581번 두 수 사이의 소수 찾기
# a = int(input())
# b = int(input())

# prime_lst = []
# sum_p = 0
# for i in range(a, b + 1):
#     not_prime = 0
#     if i > 1:
#         for j in range(2, i):
#             if i % j == 0:
#                 not_prime += 1
#                 break
#         if not_prime == 0:
#             prime_lst.append(i)
# for i in prime_lst:
#     sum_p += i

# if len(prime_lst)>0:
#     print(sum_p, prime_lst[0], sep='\n')
# else:
#     print(-1)