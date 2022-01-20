hap = 0     # 기차 탑승 인원
max = 0     # 기차 최대 탑승 인원

for i in range(10):
    # 순서대로 내린 사람, 탄 사람
    a, b = map(int, input().split())
    hap = hap - a + b

    # 최대값보다 크면 max에 대입
    if hap > max:
        max = hap

print(max)