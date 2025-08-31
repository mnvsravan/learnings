#include <stdio.h>
int main() {
    int a=72;
    int *p=&a; // pointer to a
    int **q=&p; // pointer to pointer p
    printf("The value of a is %d\n", a);
    printf("The value of a is %d\n", *p); // dereferencing pointer p
    printf("The value of a is %d\n", **(&p)); // dereferencing address of p to get value of a
    printf("The value of a is %d\n", &a); // address of a
    return 0;
}
// this ** and && can cancel each other
// so **(&p) is same as *p
// and &(*p) is same as p.