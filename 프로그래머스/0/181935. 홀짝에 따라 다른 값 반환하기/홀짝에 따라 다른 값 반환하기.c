#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

int solution(int n) {
    int answer = 0;
    
    if (n % 2 == 0) {
        for (int i = 2 ; i <= n ; i+=2) {
            answer += pow(i, 2);
        }
    }
    else {
        for (int i = 1 ; i <= n ; i+=2) {
            answer += i;
        }
    }
    
    return answer;
}