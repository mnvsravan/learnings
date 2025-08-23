#include <stdio.h>

// Function declaration
int sum(int, int);

// Function definition
int sum(int a, int b) {
    return a + b;
}

int main() {
    int a = 5;
    int b = 6;
    int c = sum(a, b);
    printf("The sum of %d and %d is %d\n", a, b, c);

    int d = 23;
    int e = 45;
    int f = sum(d, e);
    printf("The sum of %d and %d is %d\n", d, e, f);

    int g = 123;
    int h = 456;
    int i = sum(g, h);
    printf("The sum of %d and %d is %d\n", g, h, i);

    return 0;
}
