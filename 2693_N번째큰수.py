N = 3             # N번째 큰 수
T = int(input())  # 테스트 갯수

for _ in range(T):
    A = list(map(int, input().split(' ')))   # 배열
    A.sort(reverse=True)    
    if len(A) == 10:
        print(A[N-1])

# 파이썬 for문에서 변수 값이 필요 없을 때에는 _(언더바)를 사용
# Q. sort 안 쓰고 어떻게 만들지