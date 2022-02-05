# 구간의 시작과 끝을 나타내는 정수 A, B
A, B = map(int, input().split(' '))

# 구간에 속하는 숫자 만들기 (1000개)
# 1부터 44까지 만들면 990개 + 45 숫자 10개 추가
sequence = []
for i in range(45):
    for j in range(1, i+1):
        sequence.append(int(i))

for k in range(10):
    sequence.append(int(45))

# 구간에 속하는 숫자의 합
sum = 0
for i in range(A-1, B):
    sum += sequence[i]

print(sum)