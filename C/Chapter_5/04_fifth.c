#include <stdio.h>

float average(float, float, float); // Function prototype

float average(float a, float b, float c) { 
    return (a + b + c) / 3;  // correct formula
}

int main() {
    float a, b, c;
    a = 5; b = 10; c = 15;

    printf("The average of a, b and c is %f\n", average(  a,b,c));

    return 0;
}
