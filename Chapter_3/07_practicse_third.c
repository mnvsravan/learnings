#include <stdio.h>

int main() {
    int number1, number2, number3;
    printf("Enter first number: ");
    scanf("%d", &number1);
    printf("Enter second number: ");
    scanf("%d", &number2);
    printf("Enter third number: ");
    scanf("%d", &number3);
    if(number1 > number2 && number1 > number3) {
        printf("The largest number is: %d\n", number1);
    } else if (number2 >= number1 && number2 >= number3) {
        printf("The largest number is: %d\n", number2);
    } else {
        printf("The largest number is: %d\n", number3);
    }
    return 0;
}