#include <stdio.h>
int main() {

int a=4;
printf("%d %d %d", a, ++a, a++);  // Undefined behavior: modifying 'a' more than once between sequence points


    return 0;
} // The output is undefined because the order of evaluation of function arguments is not specified in C.
// so even 4 5 5 or 6 5 5 or 5 5 5 is possible.
