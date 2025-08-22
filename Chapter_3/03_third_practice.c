#include <stdio.h>

int main() {
    int marks1, marks2, marks3;
    printf("Enter marks for subject 1: ");
    scanf("%d", &marks1);
    printf("Enter marks for subject 2: ");
    scanf("%d", &marks2);
    printf("Enter marks for subject 3: ");
    scanf("%d", &marks3);
    char pass = 'Pass';
    char fail = 'Fail';
    if (marks1&& marks2 && marks3 >= 40) {
        printf("You have passed all subjects.\n");
    } else if (marks1 < 40 || marks2 < 40 || marks3 < 40) {
        printf("You have failed in one or more subjects.\n");
    } else {
        printf("Invalid marks entered.\n");
    }
    return 0;
}
