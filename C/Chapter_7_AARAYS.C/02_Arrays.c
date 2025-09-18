#include <stdio.h>

int main() {
    int marks[5];
    int i;  // loop variable

    printf("Enter the marks of 5 members:\n");

    for (i = 0; i < 5; i++) {
        scanf("%d", &marks[i]);
    }

    printf("\nThe values of marks are:\n");
    for (i = 0; i < 5; i++) {
        printf("Marks of member %d is %d\n", i + 1, marks[i]);
    }

    return 0;
}
