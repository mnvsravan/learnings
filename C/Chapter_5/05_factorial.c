#include <stdio.h>
int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1; // Base case: factorial of 0 or 1 is 1
    }
    return n * factorial(n - 1); // Recursive case
}

int main() {
    int number=5;
    printf("The factorial of %d is %d\n", number, factorial(number));
    return 0;
}
    
