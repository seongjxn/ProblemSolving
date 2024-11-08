#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
    int N;

    scanf("%d", &N);
    printf("%d", (N / 5) + (N / 25) + (N / 125));
}