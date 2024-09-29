def solution(nums):
    answer = 0
    
    # 폰켓몬 종류 개수
    num = len(list(set(nums)))
    
    # 뽑아야 하는 폰켓몬 개수
    num_pick = int(len(nums)/2)
    
    # 폰켓몬 종류가 뽑아야 하는 폰켓몬 개수 보다 많으면 그냥 폰켓몬 종류 개수
    # 왜냐하면, 우리는 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아서 폰켓몬 종류 번호의 개수를 찾는 것
    # 쉽게 말하면, 2개 뽑는데 1, 2, 3이라는 종류가 있다면 어떤 조합을 해도 1, 2 / 2, 3처럼 최대 종류 개수가 2개임
    if num > num_pick: answer = num_pick
    elif num == num_pick: answer = num_pick
    # 그런데 3개 뽑는데 종류가 2개야. 그러면 어쨋든 최대로 조합될 수 있는 최대 종류 개수는 강제로 2개가 되는거지
    else:
        answer = num
    
    return answer