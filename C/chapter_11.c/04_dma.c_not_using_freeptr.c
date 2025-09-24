#include <stdio.h>   // Standard I/O header for printf and scanf
#include <stdlib.h>  // Standard library header for malloc and free

int main() {
    int n;          // Declare an integer 'n' to store the number of elements
    int* ptr;       // Declare an integer pointer 'ptr' which will point to a dynamically allocated array

    // Take input from the user: how many integers they want in the array
    int n=7;

    // Allocate memory dynamically for 'n' integers using malloc
    // malloc returns a void pointer, so we cast it to (int*)
    ptr = (int*) malloc(n * sizeof(int));

    // Note: 'int arr[n];' is variable length array (VLA), allowed in C99,
    // but malloc is preferred when you want to allocate memory dynamically.

    // Example: Store values into the dynamically allocated array
    // Here we store 10 in ptr[0], and 20 in ptr[1]
    ptr[0] = 10;    
    ptr[1] = 20;  
    free(ptr);  

    // Print the stored values
    printf("First value = %d\n", ptr[0]);
    printf("Second value = %d\n", ptr[1]);

    // Free the allocated memory after usage to avoid memory leaks
    

    return 0;   // End of program
}
