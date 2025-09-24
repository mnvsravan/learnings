#include <stdio.h>  
// Includes the standard I/O library so we can use FILE, fopen, fscanf, printf, fclose, etc.

int main()  
// Entry point of the C program. Execution starts here.
{
    FILE *fptr;  
    // Declares a file pointer 'fptr' which will be used to refer to the file.

    int num1, num2, num3;  
    // Declares three integer variables to store values read from the file.

    fptr = fopen("file.txt", "r");  
    // Opens the file "file.txt" in read mode ("r").
    // If the file exists and opens successfully, 'fptr' will hold its reference.
    // If the file cannot be opened, 'fptr' will be NULL (good practice is to check this).

    fscanf(fptr, "%d %d %d", &num1, &num2, &num3);  
    // Reads three integers from the file using the format "%d %d %d".
    // The values read from the file are stored in num1, num2, and num3.
    // '&' is used because fscanf needs the memory address of the variables.

    printf("The values are %d %d %d \n", num1, num2, num3);  
    // Prints the three integer values stored in num1, num2, and num3.
    // "%d" is replaced by the actual integer values.
    // '\n' ensures output goes to the next line after printing.

    fclose(fptr);  
    // Closes the file "file.txt" after reading.
    // This frees the resources associated with the file.

    return 0;  
    // Returns 0 to the operating system, indicating successful execution.
}
