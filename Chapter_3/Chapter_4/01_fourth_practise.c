#include <stdio.h>

int main() {
    int i, n;
    printf("Enter the value of n: ");
    scanf("%d", &n);

    for (i = 0; i < 10; i++) {  // initialization, condition, increment
        printf("The value of %d * %d is %d\n", n, i, n * i);
    }

    return 0;  // should be after the loop
}

    
