#include <stdio.h>

int main()
{
    int arr[3][10];           // Declare a 2D array with 3 rows and 10 columns
    int mul[] = {2, 7, 9};    // Declare an array with 3 elements (multipliers)

    // Loop over each row (3 rows)
    for (int i = 0; i < 3; i++)
    {
        // Loop over each column (10 columns)
        for (int j = 0; j < 10; j++)
        {
            // Calculate and store multiplication value:
            // For row i, multiply mul[i] by (j + 1)
            arr[i][j] = mul[i] * (j + 1);
        }
    }

    // Loop again over rows to print the values stored
    for (int i = 0; i < 3; i++)
    {
        // Loop over each column
        for (int j = 0; j < 10; j++)
        {
            // Print the value of the current element in arr
            printf("The value of arr[%d][%d] is %d\n", i, j, arr[i][j]);
        }
        printf("\n");  // Print a newline after each row for better readability
    }

    return 0;  // End of program
}
