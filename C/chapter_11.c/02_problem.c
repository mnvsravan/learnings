#include <stdio.h>   // Standard Input Output header (for printf, scanf)
#include <stdlib.h>  // Standard Library header (for calloc, realloc, free)

int main()
{
    int n = 5;       // Step 1: Declare an integer 'n' with initial size = 5
    int *ptr;        // Step 2: Declare a pointer to int (will hold address of allocated memory)

    // Step 3: Dynamically allocate memory for 5 integers using calloc
    // calloc initializes the memory to 0 by default
    ptr = (int *)calloc(n, sizeof(int));

    // Step 4: Take input from user for the first 5 integers
    for (int i = 0; i < n; i++)   // Loop runs 5 times
    {
        scanf("%d", &ptr[i]);    // Store user input into ptr[i]
    }

    // Step 5: Print the entered array of 5 integers
    printf("The Array is \n");
    for (int i = 0; i < n; i++)   // Loop runs 5 times
    {
        printf("%d \n", ptr[i]); // Print each element of the array
    }

    // ---------------- Now reallocating memory ---------------- //

    n = 10;  // Step 6: Increase the size of the array to 10
    // Step 7: Use realloc to resize previously allocated memory
    // realloc(ptr, new_size) → keeps old values, adds new space
    ptr = (int*) realloc(ptr, 10 * sizeof(int));

    // Step 8: Take input for 10 integers (new inputs overwrite old ones + fill new space)
    for (int i = 0; i < n; i++)   // Loop runs 10 times
    {
        scanf("%d", &ptr[i]);    // Store user input into ptr[i]
    }

    // Step 9: Print the array of 10 integers
    printf("The Array is \n");
    for (int i = 0; i < n; i++)   // Loop runs 10 times
    {
        printf("%d \n", ptr[i]); // Print each element of the array
    }

    // Step 10: Free dynamically allocated memory (good practice to prevent memory leaks)
    free(ptr);

    return 0;   // End of program
}
