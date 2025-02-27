#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* my_string, const char* overwrite_string, int s) {
    int str_len = strlen(my_string);
    int over_len = strlen(overwrite_string);
    
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)malloc(str_len + 1);
    
    // 1) 원본 문자열의 앞부분을 answer에 복사 (s번째까지)
    strncpy(answer, my_string, s);
    answer[s] = '\0';  // 문자열 끝을 null 문자로 처리
        
    // 2) 덮어쓸 문자열을 answer에 추가
    strcat(answer, overwrite_string);
    
    // 3) 원본 문자열에서 s 이후의 부분을 answer에 추가
    strcat(answer, my_string + s + over_len);
    
    printf("%s", answer);
    
    return answer;
}