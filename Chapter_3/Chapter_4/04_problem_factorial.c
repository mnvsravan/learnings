#include <stdio.h>

int main() {
    int pdt = 1;
    for (int i = 1; i <= 8; i++) {
        pdt = pdt * i;
    }

    printf("The product of numbers from 1 to 8 is %d\n", pdt);

    return 0;  // should be after the loop
}
