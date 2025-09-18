#include <stdio.h>
int multiply_thirdty(int*);
#include <stdio.h>

int multiply_thirty(int* p) {
    return (*p * 30); // dereferencing pointer to get value and multiply by 30
}

int main() {
    int p = 5;
    printf("The value of p*30 is %d\n", multiply_thirty(&p)); // passing address of p // we use & to get address of p. // we can also write just &p and keep multiply_thirty(int* p) as multiply_thirty(int p) and it will work the same way
    return 0;
}



