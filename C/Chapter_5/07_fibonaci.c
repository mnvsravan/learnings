#include <stdio.h>
int fibonaci(int );
int fibonaci(int n) {
    if (n == 0) {
        return 0; // Base case: fib(0) = 0
    } else if (n == 1 || n == 2) {
        return n-1; // Base case: fib(1) = 1
    }
    return fibonaci(n - 1) + fibonaci(n - 2); // Recursive case
}
int main() {
    int number=7;
    printf("The %dth Fibonacci number is %d\n", number, fibonaci(number));
    return 0;
}

