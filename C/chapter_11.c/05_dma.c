#include <stdio.h>   // Required for input/output functions like printf and scanf
#include <stdlib.h>  // Required for dynamic memory functions like malloc, realloc
int main() {
    int n = 5;       // Initialize 'n' to 5 (initial size of the array)

    int* ptr;        // Declare a pointer to an integer (will point to dynamically allocated memory)

    scanf("%d", &n); // Read a value from the user and store it in 'n'
                     // This overwrites the initial value of 5

    // Allocate memory for 'n' integers
    // 'malloc' allocates uninitialized memory, unlike calloc
    ptr = (int*) malloc(n * sizeof(int));

    // Check if malloc failed (good practice)
    // if (ptr == NULL) {
    //     printf("Memory allocation failed!\n");
    //     return 1;
    // }

    ptr[0] = 3;      // Assign 3 to the first element of the dynamically allocated array

    printf("%d", ptr[0]);  // Output the value stored in ptr[0], which is 3
    // Reallocate the memory to hold 10 integers now instead of 'n'
    // realloc resizes the memory block without losing existing data (if possible)
    ptr = (int*) realloc(ptr, 10 * sizeof(int));

    // Again, it's good practice to check for NULL
    // if (ptr == NULL) {
    //     printf("Reallocation failed!\n");
    //     return 1;
    // }

    return 0;        // Indicate successful program execution
}
