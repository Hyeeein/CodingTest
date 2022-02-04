# # 두 개의 자연수를 입력 받음 (10000이하의 자연수)
# while True:
#     a, b = map(int, input().split(' '))
#     if 1 <= a <= 10000 and 1 <= b <= 10000:
#         break

# # 둘 중 큰 수가 max_num, 작은 수가 min_num
# max_num, min_num = 0, 0

# if a < b:
#     min_num = a
#     max_num = b
# else:
#     min_num = b
#     max_num = a

# ## 최대공약수 구하기
# # 최대공약수는 둘 중 작은 수보다는 무조건 작으니까 min_num부터 시작
# for i in range(min_num, 0, -1):
#     if a % i == 0 and b % i == 0:
#         print(i)
#         break

# ## 최소공배수 구하기
# # max_num부터 두 수를 곱한 수까지 반복 / 최소공배수는 max_num보다는 무조건 큼
# for i in range(max_num, a * b + 1):
#     if i % a == 0 and i % b == 0:
#         print(i)
#         break


# 왜 자꾸 시간 초과인건데에에에!!!!
# 구글링 : math 모듈의 최대공약수(gcd), 최소공배수(lcm) 모듈을 써보아라!

# 두 개의 자연수를 입력 받음 (10000이하의 자연수)
while True:
    a, b = map(int, input().split(' '))
    if 1 <= a <= 10000 and 1 <= b <= 10000:
        break

# 최대공약수, 최소공배수
import math
print(math.gcd(a, b))
print(math.lcm(a, b))