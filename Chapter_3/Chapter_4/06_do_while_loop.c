#include <stdio.h>

int main() {
    int i = 0;   // declare outside the loop
    do {
        printf("The value of i is %d\n", i);
        i++;
    } while (i < 10);
    return 0;
}


