def solution(people, limit):
    answer = 0
    
    # 1) 무게 순서대로 정렬
    people.sort()
    
    # 순서대로 더해서 limit 보다 넘으면 answer 값 하나 추가하면 22점 나옴
    # [다른 방식] 제일 첫 값과 마지막 값을 더했을 때, limit 보다 작으면 구출하고 리셋하는 방식
    start = 0
    end = len(people)-1
    while (start <= end):
        # 20, 80키로로 예를 들면 가능하면 둘이 한 번에 구출
        if (people[start]+people[end]) <= limit:
            start += 1
            end -= 1
        # 50, 80키로면 뒤에 있는 80키로라도 먼저 구출
        else:
            end -= 1
        answer += 1
        
    return answer