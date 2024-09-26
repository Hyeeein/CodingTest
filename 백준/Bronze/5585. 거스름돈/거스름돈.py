# 타로가 지불할 돈
n = int(input())
count = 0

# 동전의 종류
coin_back = 1000 - n
coin_types = [500, 100, 50, 10, 5, 1]

for coin in coin_types:
    count += coin_back // coin
    coin_back %= coin

print(count)