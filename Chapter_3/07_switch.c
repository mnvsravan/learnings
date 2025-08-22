#include <stdio.h>

int main() {
    int a;
    printf("Enter a number (1-5): ");
    scanf("%d", &a);
    switch (a) {
        case 1:
            printf("You entered one.\n");
            break;
        case 2:
            printf("You entered two.\n");
            break;
        case 3:
            printf("You entered three.\n");
            break;
        case 4:
            printf("You entered four.\n");
            break;
        case 5:
            printf("You entered five.\n");
            break;
        default:
            printf("Invalid input! Please enter a number between 1 and 5.\n");
    }
    return 0;
}
