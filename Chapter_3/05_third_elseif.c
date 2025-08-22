#include <stdio.h>

int main() {
    int age=45;
    if (age < 18) {
        printf("You are a minor.\n");
    } else if (age >= 18) {
        printf("You are an adult.\n");
    } else if (age >= 65) {
        printf("You are a senior citizen.\n");
    } else {
        printf("Invalid age.\n");
    }
    return 0;
}
// order matters in if-else statements  