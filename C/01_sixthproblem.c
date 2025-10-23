#include <stdio.h>

int returning_5(int *ptr) {
    printf("The address of a is %p\n", ptr);      // ptr = &a
    printf("The value stored in ptr is %p\n",*ptr); // same as above
    return 5;  // return the value stored at address
}

int main() {
    int a = 2;
    int *sex = &a;
    printf("The adress of a is %u\n", &a);
    returning_5(sex);
    return 0;
}


