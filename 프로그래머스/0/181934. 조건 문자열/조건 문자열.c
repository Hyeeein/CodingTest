#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* ineq, const char* eq, int n, int m) {
    int answer = 0;
    
    // 두 가지 조건을 모두 만족해야 1을 반환'
    if (strcmp(eq, "=") == 0) {
        if ((strcmp(ineq, ">") == 0 && n >= m) || (strcmp(ineq, "<") == 0 && n <= m)) {
            answer = 1;
        }
    }
    else if (strcmp(eq, "!") == 0) { // eq가 "!"인 경우
        if ((strcmp(ineq, ">") == 0 && n > m) || (strcmp(ineq, "<") == 0 && n < m)) {
            answer = 1;
        }
    }
    
    return answer;
}