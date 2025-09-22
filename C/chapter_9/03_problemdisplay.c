#include <stdio.h>  // Include standard input/output library for printf and scanf

// Define a struct for Complex numbers
typedef struct {
    int real;       // Integer to store the real part of the complex number
    int imaginary;  // Integer to store the imaginary part of the complex number
} Complex;          // 'Complex' is now a new type name we can use for variables

// Function to display a complex number
int display(Complex c) {
    // Print the complex number in the form: real + imaginary i
    printf("The value of Complex number is %d + %di\n", c.real, c.imaginary);
    return 0;  // Return 0 to indicate successful display
}

int main() {
    Complex ca[5];  // Declare an array of 5 Complex numbers to store multiple entries

    // Loop to input 5 complex numbers
    for(int i = 0; i < 5; i++) {
        // Prompt user to enter the real part of the current complex number
        printf("Enter real part for complex number %d: ", i);
        scanf("%d", &ca[i].real);  // Read an integer and store it in ca[i].real

        // Prompt user to enter the imaginary part of the current complex number
        printf("Enter imaginary part for complex number %d: ", i);
        scanf("%d", &ca[i].imaginary);  // Read an integer and store it in ca[i].imaginary
    }

    // Print a header before displaying all complex numbers
    printf("\nComplex numbers entered are:\n");

    // Loop to display all 5 complex numbers
    for(int i = 0; i < 5; i++) {
        display(ca[i]);  // Call the display function to print the i-th complex number
    }

    return 0;  // End of program
}
