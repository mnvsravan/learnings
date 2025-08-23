#include <stdio.h>

int main() {
    int n = 16;
    int isPrime = 1;  // assume n is prime

    for (int i = 2; i < n; i++) {
        if (n % i == 0) {
            isPrime = 0;  // found a divisor
            break;
        }
    }

    if (isPrime)
        printf("The number %d is a prime number\n", n);
    else
        printf("The number %d is not a prime number\n", n);

    return 0;  // should be after the loop
}

