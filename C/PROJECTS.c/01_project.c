#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int number, guess, attempts = 0;

    // Seed the random number generator with current time
    srand(time(0));
    number = rand() % 101;  // Generates random number between 0 and 100

    printf("Guess the number between 0 and 100:\n");
    scanf("%d", &guess);
    for (attempts = 1; guess != number; attempts++) {
        if (guess < number) {
            printf("Too low! Try again:\n");
        } else {
            printf("Too high! Try again:\n");
        }
        scanf("%d", &guess);  // should be after the loop
    }
    for (guess==number; guess==number; attempts++) {
        printf("Congratulations! You've guessed the number %d in %d attempts.\n", number, attempts);
        break;
    }
    return 0;  // should be after the loop
}
   
            
    


