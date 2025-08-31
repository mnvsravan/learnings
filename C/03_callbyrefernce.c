#include <stdio.h>

// Function declaration
int sum(int*, int*);

// Function definition
int sum(int* a, int* b) {// Pointers to integers // Call by reference
    *a=6;
    return (*a + *b);  // Add values pointed by a and b
}

int main() {
    int x = 10;
    int y = 20;
    printf("Sum of x and y is %d\n", sum(&x, &y)); // Call by reference 
    printf("Value of x is %d\n", x); // x is modified to 6
    return 0;
}
