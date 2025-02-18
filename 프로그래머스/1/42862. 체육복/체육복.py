def solution(n, lost, reserve):

    # 조건 5 (본인 것 잃어버린 경우, 본인 옷으로 대체)
    set_lost = set(lost) - set(reserve) # 차집합 활용하여 공통 부분 제거
    set_reserve = set(reserve) - set(lost)
    
    # 한 명씩 옷 매칭해서 제외 (여벌 가진 3번은 2번과 4번에게만 빌려줄 수 있음 !!)
    for r in set_reserve:
        if r-1 in set_lost:
            set_lost.remove(r-1)
        elif r+1 in set_lost:
            set_lost.remove(r+1)

    answer = n - len(set_lost)
            
    return answer