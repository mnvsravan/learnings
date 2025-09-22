#include <stdio.h>   // Includes the standard input/output library, 
                     // required for file operations like fopen, fprintf, fclose, etc.

int main()           // Entry point of the program, execution starts here
{
    FILE *fptr;      // Declares a pointer to FILE type, used to handle file operations

    // Opens a file named "harry.txt" in append mode ("a")
    // If the file does not exist, it will be created
    // If it exists, new content will be added at the end of the file
    fptr = fopen("harry.txt", "w");  

    int num = 432;   // Declares an integer variable 'num' and initializes it with value 432

    // Writes the value of 'num' into the file pointed by 'fptr'
    // "%d" is a format specifier for integers
    fprintf(fptr, "%d", num);  

    // Closes the file to free resources and ensure data is properly written
    fclose(fptr);    

    return 0;        // Returns 0, indicating that the program executed successfully
}
  
// this maks the harry.txt refersh and prints the num , if we use "a" instead of w it adds the value 