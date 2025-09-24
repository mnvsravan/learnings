#include <stdio.h>   // Required for input/output functions like printf and scanf
#include <stdlib.h>  // Required for memory allocation functions like calloc
int main() {
    int n;           // Declare an integer variable 'n' to store the number of elements
    int* ptr;        // Declare an integer pointer 'ptr' to point to dynamically allocated memory

    scanf("%d", &n); // Read the value of 'n' from the user input

    // Allocate memory for 'n' integers and assign the address to 'ptr'
    // calloc initializes all allocated memory to zero
    // Typecast to (int*) is optional in C, but required in C++
    ptr = (int*) calloc(n, sizeof(int));

    // Access and modify elements in the dynamically allocated memory
    ptr[0] = 3;      // Assign 3 to the first element of the allocated array
    ptr[1] = 6;      // Assign 6 to the second element of the allocated array

    // Print the value of the first element
    printf("%d", ptr[0]);

    return 0;        // Indicate that the program ended successfully
}

