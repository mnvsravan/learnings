#include <stdio.h>   // Includes standard input/output library functions 
                     // (needed for file handling like fopen, fputc, etc.)

int main()           // Entry point of the program
{
    FILE *ptr;       // Declares a pointer to FILE type, used for file operations

    // Opens the file "harry.txt" in write mode ("w")
    // If "harry.txt" exists, its content will be erased
    // If it does not exist, a new file will be created
    ptr = fopen("harry.txt", "w");

    // Example (commented out): this line would read a character from the file
    // char c = fgetc(ptr); // fgetc() reads one character at a time from the file

    // Example (commented out): this would print the character read from the file
    // printf("%c", c);      // Prints the character 'c' to the console

    // Writes a single character 'c' to the file using fputc()
    // This will store the letter 'c' inside "harry.txt"
    fputc('c', ptr);

    // Closes the file to save changes and free memory resources
    fclose(ptr);

    return 0;        // Returns 0 → indicates successful program execution
}
