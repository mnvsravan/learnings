#include <stdio.h>

int main() {
    int income = 400000;
    int Tax;

    if (income < 250000) {
        Tax = 0;
    } else if (income >= 250000 && income < 500000) {
        Tax = (income - 250000) * 0.05;
    } else if (income >= 500000 && income < 1000000) {
        Tax = (income - 500000) * 0.1 + 12500; // 12500 is the tax for first 5L
    } else {
        Tax = (income - 1000000) * 0.2 + 62500; // 62500 is the tax for first 10L
    }

    printf("The income tax is: %d\n", Tax);
    return 0;
}
