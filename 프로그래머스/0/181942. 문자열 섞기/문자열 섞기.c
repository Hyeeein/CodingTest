#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* str1, const char* str2) {
    int str_len = strlen(str1);
    
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)malloc(str_len * 2 + 1);
    
    if (!answer) return NULL; // 메모리 할당 실패 시 예외 처리
    
    for (int i=0 ; i < str_len ; i++) {
        answer[i * 2] = str1[i];
        answer[i * 2 + 1] = str2[i];
    }
    
    answer[str_len * 2] = '\0';
    
    return answer;
}