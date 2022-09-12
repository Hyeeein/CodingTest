# 9명의 키 입력
num = [int(input()) for i in range(9)]

# 전체 합에서 2명을 제외하면 합이 100
sumN = sum(num)
a, b = 0, 0

for i in range(9):
    for j in range(i+1, 9):
        if (sumN - num[i] - num[j]) == 100:
            a = num[i]
            b = num[j]
num.remove(a)   # for문에서 지워버리면 index 길이가 안 맞으니까 밖에서 remove()
num.remove(b)

# 순서대로 정렬 후 출력
num.sort()  # 변수로 저장하지 않고 sort()로 정렬만!

# 출력
for i in range(7):
    print(num[i])



# bruteforce(브루트포스):완전탐색 알고리즘 , 가능한 모든 경우의 수를 탐색하면서 요구조건에 충족하는 결과를 가져온다
# 장점 : 예외 없이 100%의 확률로 정답만 출력

# 20
# 7
# 23
# 19
# 10
# 15
# 25
# 8
# 13

# 정윤님
# height = [int(input()) for _ in range(9)]
# a1, a2 = 0, 0
# # [20,7,23,19,10,15,25,8,13]
# for i in range(len(height)):
#     for j in range(i + 1, len(height)):
#         if sum(height) - (height[i] + height[j]) == 100:
#             a1 = height[i]
#             a2 = height[j]
# height.remove(a1)
# height.remove(a2)

# for i in range(len(height)):
#     sort_height = i
#     for j in range(i + 1, len(height)):
#         if height[j] < height[sort_height]:
#             height[j], height[sort_height] = height[sort_height], height[j]
# print('\n'.join(map(str, height)))

