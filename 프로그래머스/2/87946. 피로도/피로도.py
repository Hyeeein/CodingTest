from itertools import permutations

def solution(k, dungeons):
    answer = -1

    # 던전 탐험 모든 경우의 수 구하기 (순열 사용)
    for perm in permutations(dungeons):
        cnt, kk = 0, k # 하나의 경우의 수 실행마다 초기화
        for i, j in perm:
            if kk >= i:
                kk-= j
                cnt += 1
        answer = max(answer, cnt)
    
    return answer