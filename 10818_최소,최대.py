# 첫째 줄에 입력한 정수의 갯수
while True :
    N = int(input())
    if 1 <= N <= 1000000:
        break

# 둘째 줄에 입력한 N개의 정수
num = input()
int_list = num.split(' ')

# str -> int 형으로 변환
new_list = []
for i in int_list:
    new_list.append(int(i))

# 리스트 정렬 후 최솟값과 최댓값 출력
new_list.sort()
print(f'{new_list[0]} {new_list[len(new_list)-1]}')