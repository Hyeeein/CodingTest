from itertools import permutations # 순열

def is_prime(n):
    '''소수 판별 함수'''
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1): # 제곱근까지만 확인
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    
    # 순열을 활용해 모든 조합 찾기
    numbers_list = [int(i) for i in numbers]  # 각 하나의 숫자로 변환
    numbers_list_new = []
    
    for i in range(1, len(numbers_list)+1):
            new = list(permutations(numbers_list, i))
            
            for j in range(len(new)):
                numbers_list_new.append(new[j])
    
    # 가능한 조합의 수로 변환(join, map 활용)
    final_numbers = []  # [17, 1, 7, 71]
    
    for i in numbers_list_new:
        final_numbers.append(int(''.join(map(str, list(i)))))  # 정수로 변환 + 0도 추가로 제거 
        
    final_numbers = list(set(final_numbers)) # 중복 제거
    
    # 소수인지 확인 후 count
    for num in final_numbers:
        if is_prime(num): answer += 1

    return answer