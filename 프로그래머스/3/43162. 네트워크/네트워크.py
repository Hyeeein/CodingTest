def solution(n, computers):
    answer = 0
    visited = [False] * n  # 방문 여부 저장
    
    def dfs(node):
        visited[node] = True # 방문 처리
        for i in range(n):
            # 연결된 관계 혹은 visited[node]가 False라면
            if computers[node][i] == 1 and not visited[i]:
                dfs(i) # 노드들 방문 후 방문 처리 진행
    
    for i in range(n):
        # visited가 False라면 (방문하지 않은 노드라면)
        if not visited[i]:
            dfs(i)
            answer += 1
                
    return answer

# DFS 실행 과정
# 0번 노드 방문 → 1번 노드 연결 → 1번 노드 방문 → (연결된 노드가 더 없음 → 종료) → 첫 번째 네트워크 발견
# 2번 노드 방문 (아직 방문 안 됨) → 두 번째 네트워크 발견
# 최종 return 2
