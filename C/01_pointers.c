#include <stdio.h>
int main() {
    int a=72;
    int *p=&a; // pointer variable p holds the address of a
    int k=67;
    int*k1=&k; // pointer variable k1 holds the address of k
    printf("The adress of a is %p\n",&a);
    printf("The adress of a is %p\n",p);
    printf("The adress of a is %p\n",&k);
    printf("The value of adress of p is %d\n",*p); // dereferencing pointer p to get the value of a
    printf("The value of adress of p is %d\n",*(&a)); // dereferencing address of a to get the value of a
    return 0;
}
// we use %p format specifier to print address in C or even %u can be used
// we use * to dereference a pointer to get the value at that address
// we use & to get the address of a variable
// pointer variable can only hold the address of a variable of same data type
// so int *p can only hold the address of int variable
// we can use it for float, char, double etc. by changing the data type accordingly
// we can also use void pointer to hold the address of any data type but we cannot dereference it directly
// we need to typecast it to the appropriate data type before dereferencing
// for example:
// void *vp;
// int a=10;
// vp=&a; // valid  // void pointer can hold the address of int variable    
// printf("%d",*vp); // invalid // cannot dereference void pointer directly
// printf("%d",*(int*)vp); // valid // typecasting void pointer to int pointer before dereferencing
