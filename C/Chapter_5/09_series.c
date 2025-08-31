#include <stdio.h>
int sum(int);
int sum(int n) {
    if (n == 1) {
        return 1; // Base case: sum of first 1 natural number is 1
    }
    return n    + sum(n - 1); // Recursive case
}
int main() {
    int number=5;
    printf("The sum of first %d natural numbers is %d\n", number, sum(number));
    return 0;
}
