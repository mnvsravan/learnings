#include <stdio.h>

float force(float); // Function prototype
float force(float mass) {
    return mass * 9.8; // F = m * g, where g = 9.8 m/s^2
}
int main() {
    float mass = 10.0; // mass in kilograms
    printf("The force on a mass of %.2f kg is %.2f N\n", mass, force(mass));
    return 0;
}
