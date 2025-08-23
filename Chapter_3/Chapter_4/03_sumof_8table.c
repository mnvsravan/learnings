#include <stdio.h>

int main() {
    int sum = 0;
    for (int i = 1; i <= 8; i++) {
        sum = sum + i * 8;
        printf("The value of 8 * %d is %d | Running sum = %d\n", i, i * 8, sum);
    }

    return 0;  // correctly placed after loop
}
