def solution(sizes):
    answer = 0
    
    w_list = []
    h_list = []
    
    for size in sizes:
        # 큰 값들은 다 왼쪽으로 넘기기
        if size[0] < size[1]:
            tmp = size[0]
            size[0] = size[1]
            size[1] = tmp
        
        w_list.append(size[0])
        h_list.append(size[1])
    
    answer = max(w_list) * max(h_list)
    
    return answer