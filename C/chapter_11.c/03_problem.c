#include <stdio.h>   // provides declarations for input/output functions: printf, fprintf, etc.
#include <stdlib.h>  // provides declarations for memory functions: calloc, realloc, free

int main(void)
{
    int n = 10;            // set initial array size to 10 (user requested change from 5 -> 10)
    int *ptr = NULL;       // pointer that will hold the address of dynamically allocated memory

    /* Allocate memory for 'n' integers.
       calloc(n, sizeof(int)) allocates contiguous memory for n elements and initializes all bytes to zero.
       Casting to (int *) is optional in C but shown here for clarity. */
    ptr = (int *) calloc(n, sizeof(int));

    /* Check if calloc returned NULL (allocation failed). If it failed, print an error and exit with non-zero code. */
    if (ptr == NULL)
    {
        fprintf(stderr, "Memory allocation failed\n"); // print error to stderr
        return 1;                                     // exit program with error code
    }

    /* Fill the allocated array with values.
       The formula used: ptr[i] = 7 * (i + 1).
       - i starts at 0, so (i + 1) produces 1,2,... which gives 7,14,... */
    for (int i = 0; i < n; i++)    // loop from i = 0 to i = n-1
    {
        ptr[i] = 7 * (i + 1);      // set element i to 7 times (i+1)
    }

    /* Print the array contents after initial fill. */
    printf("The Array is (after initial fill):\n"); // header for clarity
    for (int i = 0; i < n; i++)                      // loop through all n elements
    {
        printf("%d\n", ptr[i]);                      // print each integer on its own line
    }

    /* Now increase the logical size of the array to 15 as requested.
       Update the variable 'n' to reflect the new desired size. */
    n = 15;

    /* Use realloc to resize the previously allocated block.
       IMPORTANT: realloc may move the block to a new location, so we use a temporary pointer to check for failure.
       If realloc fails it returns NULL and the original ptr remains valid (must be freed). */
    int *temp = (int *) realloc(ptr, n * sizeof(int)); // attempt to resize to hold 15 integers

    if (temp == NULL)         // check if realloc failed
    {
        fprintf(stderr, "Memory reallocation failed\n"); // print error
        free(ptr);              // free original memory to avoid leak
        return 1;               // exit with error
    }

    ptr = temp;                // assign resized block to ptr (realloc succeeded)

    /* Initialize (or reinitialize) elements of the resized array.
       We assign ptr[i] = 7 * (i + 1) for i = 0..n-1.
       Note: realloc preserves previous contents for indices < old_size, but here we reassign all for consistency. */
    for (int i = 0; i < n; i++)   // loop through all 15 positions
    {
        ptr[i] = 7 * (i + 1);     // set each element to 7*(i+1)
    }

    /* Print the array contents after resizing and filling. */
    printf("The Array is (after realloc to %d):\n", n); // show new size in header
    for (int i = 0; i < n; i++)                         // loop through all n (now 15) elements
    {
        printf("%d\n", ptr[i]);                         // print each element
    }

    free(ptr);   // free the dynamically allocated memory when finished (prevents memory leaks)
    return 0;    // return 0 to indicate successful program termination
}

