N = 3             # N번째 큰 수
T = int(input())  # 테스트 갯수

for _ in range(T):
    A = list(map(int, input().split(' ')))   # 배열
    A.sort(reverse=True)    
    if len(A) == 10:
        print(A[N-1])

# 파이썬 for문에서 변수 값이 필요 없을 때에는 _(언더바)를 사용
# Q. sort 안 쓰고 어떻게 만들지



#### ---------------------------------------------- ####
# 정윤님

# # 방법1
# t = int(input())
# for _ in range(t):
#     a = list(map(int, input().split()))
#     a.sort()
#     print(a[-3])

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    if len(a[i]) != 10:
        print('배열 열 개 입력하세요!')
        break
    else:
        a[i].sort()
        print(a[i][-3])

# try:
#     for i in range(n):
#         if len(a[i]) != 10:
#             raise Exception('10개의 배열을 입력해 주세요')
#         else:
#             a[i].sort()
#             print(a[i][-3])
# except Exception as e:
#     print(e)



### sort 안 쓴 것 ###

tmp = 0
res = []
for _ in range(int(input())):
  l = list(map(int, input().split())) 
  for i in range(10):
    for j in range(i, 10):
      if l[i] > l[j]:
        tmp = l[i]
        l[i] = l[j]
        l[j] = tmp
  print(l[7])
