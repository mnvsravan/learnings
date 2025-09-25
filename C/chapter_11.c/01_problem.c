#include <stdio.h>   // Header file for standard input/output functions (printf, scanf)
#include <stdlib.h>  // Header file for memory allocation functions (malloc, free)

int main()
{
    int n = 6;       // Declare an integer 'n' and initialize it with 6 (number of elements)
    int *ptr;        // Declare an integer pointer 'ptr' to store the base address of allocated memory

    // Allocate memory dynamically for 'n' integers
    // malloc() returns a void pointer, so we typecast it to (int*)
    // The size allocated = n * sizeof(int) = 6 * size of int (typically 24 bytes if int = 4 bytes)
    ptr = (int *)malloc(n * sizeof(int));

    // First for loop: take input values from the user and store them in the dynamically allocated array
    for (int i = 0; i < n; i++)
    {
        // &ptr[i] = address of the i-th element in the array
        // scanf stores the entered value at that memory location
        scanf("%d", &ptr[i]);
    }

    // Second for loop: print the values stored in the array
    for (int i = 0; i < n; i++)
    {
        // ptr[i] accesses the value stored at the i-th index
        printf("%d \n", ptr[i]);
    }

    // Free the dynamically allocated memory to avoid memory leaks
    free(ptr);

    return 0;   // Program ends successfully
}
