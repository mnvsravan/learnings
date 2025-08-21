#include <stdio.h>

int main(){
    int celcius; // Declare variable for Celsius temperature
    celcius = 25; // Initialize Celsius temperature with a value
    int fahrenheit; // Declare variable for Fahrenheit temperature
    fahrenheit = (celcius * 9/5) + 32; // Convert Celsius to Fahrenheit
    printf("The temperature in Fahrenheit is: %d\n", fahrenheit); // Print the converted temperature
    
    return 0;
}
