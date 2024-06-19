# 예제 3-1. 거스름돈

n = 1260  # 거스름돈 총액
count = 0 # 거스름돈 갯수

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin    # 몫
    n %= coin             # 나머지

print(count)