#include <stdio.h>
void swap(int*, int*); // Function prototype
void swap(int* x, int* y) {
    int temp = *x; // Store the value at address x in temp
    *x = *y;       // Copy the value at address y to address x
    *y = temp;     // Copy the value in temp to address y
}
int main() {
    int a = 5, b = 10;
    swap(&a, &b); // Call swap with addresses of a and b
    printf("Before swap: a = %d, b = %d\n", a, b);
    
    

    return 0;
}
